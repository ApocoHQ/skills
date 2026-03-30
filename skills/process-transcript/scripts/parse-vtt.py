#!/usr/bin/env python3
"""Parse VTT (Teams) transcripts into Markdown files with YAML frontmatter."""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path


def parse_vtt(path: Path, output_dir: Path | None = None) -> Path:
    if not path.exists():
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    if path.suffix.lower() != ".vtt":
        print(f"Error: expected .vtt file, got: {path.name}", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding="utf-8")

    # Split into cue blocks (separated by blank lines)
    blocks = re.split(r"\n\n+", text.strip())

    utterances: list[tuple[str, str]] = []  # (speaker, text)

    for block in blocks:
        lines = block.strip().splitlines()
        if not lines or lines[0].startswith("WEBVTT"):
            continue

        content_lines = []
        for line in lines:
            if "/" in line and re.match(r"[0-9a-f]{8}-", line):
                continue
            if "-->" in line:
                continue
            content_lines.append(line)

        if not content_lines:
            continue

        raw = " ".join(content_lines)

        m = re.match(r"<v ([^>]+)>(.*?)(?:</v>)?$", raw, re.DOTALL)
        if m:
            speaker = m.group(1).strip()
            said = m.group(2).strip()
        else:
            speaker = "?"
            said = raw.strip()

        said = re.sub(r"</?v[^>]*>", "", said).strip()
        if not said:
            continue

        if utterances and utterances[-1][0] == speaker:
            utterances[-1] = (speaker, utterances[-1][1] + " " + said)
        else:
            utterances.append((speaker, said))

    # Extract date from file modification time
    mtime = path.stat().st_mtime
    date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")

    # Extract attendees
    speakers = sorted(set(s for s, _ in utterances))

    # Build markdown with frontmatter
    lines_out: list[str] = []
    lines_out.append("---")
    lines_out.append(f'date: "{date_str}"')
    lines_out.append("attendees:")
    for s in speakers:
        lines_out.append(f"  - {s}")
    lines_out.append("---")
    lines_out.append("")
    lines_out.append("## Transcript")
    lines_out.append("")
    for speaker, said in utterances:
        lines_out.append(f"{speaker}: {said}")
        lines_out.append("")

    # Write .md file to output dir (or next to the .vtt file)
    if output_dir:
        out_path = output_dir / (path.stem + ".md")
    else:
        out_path = path.with_suffix(".md")
    out_path.write_text("\n".join(lines_out), encoding="utf-8")
    print(f"{path.name} -> {out_path.name}")
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse VTT (Teams) transcripts into Markdown files with YAML frontmatter.",
    )
    parser.add_argument(
        "files",
        nargs="+",
        metavar="FILE",
        help=".vtt file(s) to parse",
    )
    parser.add_argument(
        "--output-dir",
        metavar="DIR",
        help="Directory to write .md files to (default: next to input .vtt)",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir) if args.output_dir else None
    for filepath in args.files:
        parse_vtt(Path(filepath), output_dir=output_dir)


if __name__ == "__main__":
    main()

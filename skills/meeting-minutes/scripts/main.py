#!/usr/bin/env python3
"""Strip VTT metadata from a WebVTT transcript, keeping only speaker-attributed speech."""

import re
import sys
from pathlib import Path


def strip_vtt(text: str) -> str:
    lines = text.splitlines()[4:]

    output = []
    cooldown = 0

    fragmented_line = ""
    finish_line = False

    for line in lines:
        cleaned = line.strip()

        # Skip boilerplate lines
        if not cleaned:
            cooldown = 3

        if cooldown > 0:
            cooldown -= 1
            continue

        if cleaned.endswith("</v>"):
            finish_line = True
            cleaned = cleaned[:-4].strip()

        if cleaned.startswith("<v "):
            match = re.match(r"^(<[^>]+>)\s*(.*)$", cleaned)
            if match:
                tag, message = match.group(1), match.group(2).strip()
                tag = "<" + tag[3:]

                cleaned = message
            else:
                print("Warning: line does not match expected format, skipping:", line)
                continue
        elif not cleaned:
            continue
        else:
            cleaned = " " + cleaned

        fragmented_line += cleaned  

        if not finish_line:
            continue

        if output and output[-1].startswith(tag):
            output[-1] = f"{output[-1]} {fragmented_line.strip()}"
        else:
            output.append(f"{tag} {fragmented_line.strip()}") 
        
        fragmented_line = ""
        finish_line = False

    return "\n".join(output)


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.vtt> <output.txt>", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.exists():
        print(f"Error: {input_path} not found", file=sys.stderr)
        sys.exit(1)

    text = input_path.read_text(encoding="utf-8")
    result = strip_vtt(text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result, encoding="utf-8")

    # Report stats
    original_lines = len(text.splitlines())
    result_lines = len(result.splitlines())
    print(f"Stripped {original_lines} -> {result_lines} lines ({input_path} -> {output_path})")


if __name__ == "__main__":
    main()

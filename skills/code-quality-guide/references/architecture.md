---
domain: architecture
last-reviewed: 2026-03-26
status: draft
sources: [meeting-2026-03-23-ai-best-practices, linkedin-manager domain patterns]
---

## Stance
Small modules, explicit interfaces, clear boundaries. Agents reason locally — they write great functions but create terrible architecture. Large files exceed what an agent can hold in context, making edits unreliable. Implicit patterns (convention-based routing, magic strings, inheritance hierarchies) are invisible to agents. But these are good engineering principles regardless — clear boundaries make any system maintainable.

## What to Look For
- Modules are small and single-purpose — each file does one thing and stays under 300-400 lines
- Interfaces are explicit exports or type definitions — never inferred from call-site usage or convention
- Dependencies point inward — domain logic has zero imports from infrastructure; controllers and adapters depend on domain, never the reverse
- Components are swappable black boxes — understand what a module does from its interface; change its internals without breaking consumers
- Composition over inheritance — behavior is assembled from small pieces, not extended from base classes
- Consistent layering throughout — the same architectural pattern (e.g., controller → service → repository) applies everywhere
- Side effects are pushed to the edges — the core logic is pure; I/O, state mutation, and external calls happen in the outer layers

## Red Flags
- Circular dependencies or modules importing each other's internals
- God objects with too many responsibilities
- Deep inheritance hierarchies
- Shotgun surgery — a single feature change requires touching many modules
- Business logic in the wrong layer — domain rules in controllers, data access mixed with business logic
- Hidden coupling through shared mutable state or globals
- Feature envy — a module that reaches into another module's data more than its own

## See Also
- **code-readability** — module boundaries are structural readability

## Known Gaps
- When monolithic files are acceptable
- How to handle cross-cutting concerns cleanly
- Microservices vs monolith guidance
- How to handle shared utilities without creating a junk-drawer module
- Composition patterns — when to use DI, factory functions, or event-driven wiring

---
domain: architecture
last-reviewed: 2026-03-26
---

## Stance
Small modules, explicit interfaces, clear boundaries. Agents reason locally — they write great functions but create terrible architecture. Large files exceed what an agent can hold in context, making edits unreliable. Implicit patterns (convention-based routing, magic strings, inheritance hierarchies) are invisible to agents. But these are good engineering principles regardless — clear boundaries make any system maintainable.

## What to Look For
- Modules are small and single-purpose — each file does one thing and stays under 300-400 lines
- Interfaces are explicit exports or type definitions — never inferred from call-site usage or convention
- Dependencies point inward — domain logic has zero imports from infrastructure; controllers and adapters depend on domain, never the reverse. The gold standard: a domain package with zero external dependencies
- Components are swappable black boxes — understand what a module does from its interface; change its internals without breaking consumers
- Composition over inheritance — behavior is assembled from small pieces, not extended from base classes. Exception: abstract base classes for genuine shared behavior (e.g., AggregateRoot providing event collection) are appropriate when the hierarchy is shallow and the abstraction is stable
- Consistent layering throughout — the same architectural pattern (e.g., router → service → DAO) applies everywhere
- Side effects are pushed to the edges — the core logic is pure; I/O, state mutation, and external calls happen in the outer layers
- Vertical slicing over horizontal layering — organize features as complete slices (service + domain aggregate + types per module) rather than grouping all services in one place, all repositories in another. Each slice contains everything for one feature
- Composition roots assemble dependencies — a single factory function per entry point (server, workers, tests) wires all dependencies explicitly. No DI container magic, no service locator. Constructor injection with factory functions
- Multiple entry points share one context interface — HTTP server, background workers, MCP server, and tests all consume the same `Context` type but wire it differently at their composition root
- Event-driven communication for cross-module workflows — when modules need to coordinate, they publish domain events rather than calling each other directly. A saga or orchestrator consumes events and enqueues follow-up work

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
- Microservices vs monolith guidance
- How to handle shared utilities without creating a junk-drawer module

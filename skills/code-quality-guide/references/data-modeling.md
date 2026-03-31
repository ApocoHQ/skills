---
domain: data-modeling
last-reviewed: 2026-03-26
---

## Stance
Schema is architecture — treat it with the same rigor as code structure. Agents treat schema as an afterthought — they'll add columns without considering migration safety, data integrity, or whether the schema reflects the domain. Bad schema decisions are among the hardest to reverse — a column you add carelessly today becomes a migration nightmare tomorrow.

## What to Look For
- Every migration is reversible — each up migration has a corresponding down migration; destructive operations (drop column, drop table) include a data backup strategy
- Data integrity constraints live at the database level — foreign keys, unique constraints, check constraints, and NOT NULL are enforced by the DB, not just application code. Know your database's defaults — e.g., PostgreSQL automatically indexes primary keys and unique constraints, so explicit indexes on foreign keys aren't needed
- Indexes exist for every query pattern in hot paths — no missing indexes on columns used in WHERE, JOIN, or ORDER BY clauses for common operations
- Schema reflects domain language — table and column names match the business domain, not internal implementation terms
- Migrations are tested in a staging environment before production — including rollback verification. E2E tests that run migrations against isolated schemas per test suite serve as a lightweight migration verification
- Normalize by default — denormalization requires explicit justification documenting the performance need and the consistency trade-off. Junction tables with composite primary keys for many-to-many relationships
- Nullable columns are intentional — NULL means something in the domain, not "we didn't decide yet"
- Type-safe ORM with schema-derived types — use ORM features like Drizzle's `$inferSelect`/`$inferInsert` to derive TypeScript types directly from the schema definition, eliminating type/schema drift
- Time-series data uses snapshot tables — for tracking metrics over time (follower counts, connection counts), use dedicated snapshot tables with a `recordedAt` timestamp rather than overwriting current values
- Event-sourced persistence as a hybrid pattern — domain aggregates emit events expressing state changes; DAOs pattern-match on event types and translate them to database mutations. This keeps domain logic pure while using traditional CRUD storage underneath

## Red Flags
- JSON blob columns used to avoid proper schema design
- Manually maintaining TypeScript types that duplicate what the ORM schema already defines
- Overwriting historical data instead of appending snapshots when history matters

## See Also
- **api-design** — API responses should not expose raw schema; API models are their own layer

## Known Gaps
- Multi-tenant schema strategies
- When denormalization is justified

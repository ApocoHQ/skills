---
domain: data-modeling
last-reviewed: 2026-03-26
status: draft
sources: [linkedin-manager domain patterns, industry practices]
---

## Stance
Schema is architecture — treat it with the same rigor as code structure. Agents treat schema as an afterthought — they'll add columns without considering migration safety, data integrity, or whether the schema reflects the domain. Bad schema decisions are among the hardest to reverse — a column you add carelessly today becomes a migration nightmare tomorrow.

## What to Look For
- Every migration is reversible — each up migration has a corresponding down migration; destructive operations (drop column, drop table) include a data backup strategy
- Data integrity constraints live at the database level — foreign keys, unique constraints, check constraints, and NOT NULL are enforced by the DB, not just application code
- Indexes exist for every query pattern in hot paths — no missing indexes on columns used in WHERE, JOIN, or ORDER BY clauses for common operations
- Schema reflects domain language — table and column names match the business domain, not internal implementation terms
- Migrations are tested in a staging environment before production — including rollback verification
- Normalize by default — denormalization requires explicit justification documenting the performance need and the consistency trade-off
- Nullable columns are intentional — NULL means something in the domain, not "we didn't decide yet"

## Red Flags
- JSON blob columns used to avoid proper schema design

## See Also
- **api-design** — API responses should not expose raw schema; API models are their own layer

## Known Gaps
- Event sourcing vs traditional CRUD guidance
- Time-series data patterns
- Multi-tenant schema strategies
- When denormalization is justified

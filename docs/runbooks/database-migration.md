# Operations Runbook: Zero-Downtime Database Migrations

## 1. Expand and Contract Pattern
1. **Phase 1 (Expand)**: Add new columns, tables, or non-breaking constraints. Columns must be nullable or have safe defaults.
2. **Phase 2 (Dual-Write)**: Application services write to both old and new data structures.
3. **Phase 3 (Backfill)**: Run background migration scripts to backfill existing historical records.
4. **Phase 4 (Contract)**: Update application to read exclusively from the new structure, then drop legacy columns.

## 2. Migration Execution Command
```bash
# Run migration script against isolated service database
psql -h localhost -U cloudmart_user -d <service>_db -f services/<service>/repositories/migrations.sql
```

-- =============================================================
-- PostgreSQL Migration Schema for Notification & Messaging Service
-- Database Target: notification_db
-- Version: 1.0.0 (Baseline)
-- =============================================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "btree_gist";

-- -------------------------------------------------------------
-- Table: notification_messages (Primary Aggregate Table)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS notification_messages (
    id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid()::text,
    tenant_id VARCHAR(50) NOT NULL DEFAULT 'default',
    name VARCHAR(150) NOT NULL,
    code VARCHAR(50) NOT NULL UNIQUE,
    status VARCHAR(30) NOT NULL DEFAULT 'DRAFT',
    category VARCHAR(50) NOT NULL DEFAULT 'STANDARD',
    version INTEGER NOT NULL DEFAULT 1,
    description TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    is_deleted BOOLEAN NOT NULL DEFAULT FALSE,
    deleted_at TIMESTAMPTZ,
    attributes_json JSONB NOT NULL DEFAULT '{"metadata": {}}'::jsonb,
    status_history_json JSONB NOT NULL DEFAULT '[]'::jsonb,
    custom_field_column_1 VARCHAR(255) DEFAULT 'default_val_1',
    custom_field_column_2 VARCHAR(255) DEFAULT 'default_val_2',
    custom_field_column_3 VARCHAR(255) DEFAULT 'default_val_3',
    custom_field_column_4 VARCHAR(255) DEFAULT 'default_val_4',
    custom_field_column_5 VARCHAR(255) DEFAULT 'default_val_5',
    custom_field_column_6 VARCHAR(255) DEFAULT 'default_val_6',
    custom_field_column_7 VARCHAR(255) DEFAULT 'default_val_7',
    custom_field_column_8 VARCHAR(255) DEFAULT 'default_val_8',
    custom_field_column_9 VARCHAR(255) DEFAULT 'default_val_9',
    custom_field_column_10 VARCHAR(255) DEFAULT 'default_val_10',
    custom_field_column_11 VARCHAR(255) DEFAULT 'default_val_11',
    custom_field_column_12 VARCHAR(255) DEFAULT 'default_val_12',
    custom_field_column_13 VARCHAR(255) DEFAULT 'default_val_13',
    custom_field_column_14 VARCHAR(255) DEFAULT 'default_val_14',
    custom_field_column_15 VARCHAR(255) DEFAULT 'default_val_15',
    custom_field_column_16 VARCHAR(255) DEFAULT 'default_val_16',
    custom_field_column_17 VARCHAR(255) DEFAULT 'default_val_17',
    custom_field_column_18 VARCHAR(255) DEFAULT 'default_val_18',
    custom_field_column_19 VARCHAR(255) DEFAULT 'default_val_19',
    custom_field_column_20 VARCHAR(255) DEFAULT 'default_val_20',
    custom_field_column_21 VARCHAR(255) DEFAULT 'default_val_21',
    custom_field_column_22 VARCHAR(255) DEFAULT 'default_val_22',
    custom_field_column_23 VARCHAR(255) DEFAULT 'default_val_23',
    custom_field_column_24 VARCHAR(255) DEFAULT 'default_val_24',
    custom_field_column_25 VARCHAR(255) DEFAULT 'default_val_25',
    custom_field_column_26 VARCHAR(255) DEFAULT 'default_val_26',
    custom_field_column_27 VARCHAR(255) DEFAULT 'default_val_27',
    custom_field_column_28 VARCHAR(255) DEFAULT 'default_val_28',
    custom_field_column_29 VARCHAR(255) DEFAULT 'default_val_29',
    custom_field_column_30 VARCHAR(255) DEFAULT 'default_val_30',
    custom_field_column_31 VARCHAR(255) DEFAULT 'default_val_31',
    custom_field_column_32 VARCHAR(255) DEFAULT 'default_val_32',
    custom_field_column_33 VARCHAR(255) DEFAULT 'default_val_33',
    custom_field_column_34 VARCHAR(255) DEFAULT 'default_val_34',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_notification_messages_tenant ON notification_messages (tenant_id);
CREATE INDEX IF NOT EXISTS idx_notification_messages_status ON notification_messages (status);
CREATE INDEX IF NOT EXISTS idx_notification_messages_category ON notification_messages (category);
CREATE INDEX IF NOT EXISTS idx_notification_messages_created_at ON notification_messages (created_at DESC);
CREATE INDEX IF NOT EXISTS idx_notification_messages_attributes_gin ON notification_messages USING gin (attributes_json);

-- -------------------------------------------------------------
-- Table: notification_messages_sub1 (Child Entity 1)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS notification_messages_sub1 (
    id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid()::text,
    parent_id VARCHAR(36) NOT NULL REFERENCES notification_messages(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(50) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    priority INTEGER NOT NULL DEFAULT 10,
    config_json JSONB NOT NULL DEFAULT '{}'::jsonb,
    sub1_param_1 VARCHAR(100) DEFAULT 'param_val_1',
    sub1_param_2 VARCHAR(100) DEFAULT 'param_val_2',
    sub1_param_3 VARCHAR(100) DEFAULT 'param_val_3',
    sub1_param_4 VARCHAR(100) DEFAULT 'param_val_4',
    sub1_param_5 VARCHAR(100) DEFAULT 'param_val_5',
    sub1_param_6 VARCHAR(100) DEFAULT 'param_val_6',
    sub1_param_7 VARCHAR(100) DEFAULT 'param_val_7',
    sub1_param_8 VARCHAR(100) DEFAULT 'param_val_8',
    sub1_param_9 VARCHAR(100) DEFAULT 'param_val_9',
    sub1_param_10 VARCHAR(100) DEFAULT 'param_val_10',
    sub1_param_11 VARCHAR(100) DEFAULT 'param_val_11',
    sub1_param_12 VARCHAR(100) DEFAULT 'param_val_12',
    sub1_param_13 VARCHAR(100) DEFAULT 'param_val_13',
    sub1_param_14 VARCHAR(100) DEFAULT 'param_val_14',
    sub1_param_15 VARCHAR(100) DEFAULT 'param_val_15',
    sub1_param_16 VARCHAR(100) DEFAULT 'param_val_16',
    sub1_param_17 VARCHAR(100) DEFAULT 'param_val_17',
    sub1_param_18 VARCHAR(100) DEFAULT 'param_val_18',
    sub1_param_19 VARCHAR(100) DEFAULT 'param_val_19',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_notification_messages_sub1_parent ON notification_messages_sub1 (parent_id);

-- -------------------------------------------------------------
-- Table: notification_messages_sub2 (Child Entity 2)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS notification_messages_sub2 (
    id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid()::text,
    parent_id VARCHAR(36) NOT NULL REFERENCES notification_messages(id) ON DELETE CASCADE,
    label VARCHAR(100) NOT NULL,
    value_payload TEXT NOT NULL,
    score DOUBLE PRECISION NOT NULL DEFAULT 1.0,
    tags_json JSONB NOT NULL DEFAULT '[]'::jsonb,
    sub2_metric_1 NUMERIC(12, 4) DEFAULT 1.5000,
    sub2_metric_2 NUMERIC(12, 4) DEFAULT 2.5000,
    sub2_metric_3 NUMERIC(12, 4) DEFAULT 3.5000,
    sub2_metric_4 NUMERIC(12, 4) DEFAULT 4.5000,
    sub2_metric_5 NUMERIC(12, 4) DEFAULT 5.5000,
    sub2_metric_6 NUMERIC(12, 4) DEFAULT 6.5000,
    sub2_metric_7 NUMERIC(12, 4) DEFAULT 7.5000,
    sub2_metric_8 NUMERIC(12, 4) DEFAULT 8.5000,
    sub2_metric_9 NUMERIC(12, 4) DEFAULT 9.5000,
    sub2_metric_10 NUMERIC(12, 4) DEFAULT 10.5000,
    sub2_metric_11 NUMERIC(12, 4) DEFAULT 11.5000,
    sub2_metric_12 NUMERIC(12, 4) DEFAULT 12.5000,
    sub2_metric_13 NUMERIC(12, 4) DEFAULT 13.5000,
    sub2_metric_14 NUMERIC(12, 4) DEFAULT 14.5000,
    sub2_metric_15 NUMERIC(12, 4) DEFAULT 15.5000,
    sub2_metric_16 NUMERIC(12, 4) DEFAULT 16.5000,
    sub2_metric_17 NUMERIC(12, 4) DEFAULT 17.5000,
    sub2_metric_18 NUMERIC(12, 4) DEFAULT 18.5000,
    sub2_metric_19 NUMERIC(12, 4) DEFAULT 19.5000,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_notification_messages_sub2_parent ON notification_messages_sub2 (parent_id);

-- -------------------------------------------------------------
-- Table: notification_messages_outbox (Transactional Outbox Pattern)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS notification_messages_outbox (
    id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid()::text,
    aggregate_type VARCHAR(50) NOT NULL,
    aggregate_id VARCHAR(36) NOT NULL,
    event_type VARCHAR(100) NOT NULL,
    payload JSONB NOT NULL,
    correlation_id VARCHAR(36) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'PENDING',
    retry_count INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    published_at TIMESTAMPTZ
);
CREATE INDEX IF NOT EXISTS idx_notification_messages_outbox_status ON notification_messages_outbox (status, created_at);

-- -------------------------------------------------------------
-- Data Seeding: Default Enterprise Seed Records
-- -------------------------------------------------------------
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0001', 'default', 'Seed NotificationMessage 1', 'SEED-NOT-0001', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0002', 'default', 'Seed NotificationMessage 2', 'SEED-NOT-0002', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0003', 'default', 'Seed NotificationMessage 3', 'SEED-NOT-0003', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0004', 'default', 'Seed NotificationMessage 4', 'SEED-NOT-0004', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0005', 'default', 'Seed NotificationMessage 5', 'SEED-NOT-0005', 'DRAFT', 'PREMIUM', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0006', 'default', 'Seed NotificationMessage 6', 'SEED-NOT-0006', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0007', 'default', 'Seed NotificationMessage 7', 'SEED-NOT-0007', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0008', 'default', 'Seed NotificationMessage 8', 'SEED-NOT-0008', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0009', 'default', 'Seed NotificationMessage 9', 'SEED-NOT-0009', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0010', 'default', 'Seed NotificationMessage 10', 'SEED-NOT-0010', 'ACTIVE', 'PREMIUM', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0011', 'default', 'Seed NotificationMessage 11', 'SEED-NOT-0011', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0012', 'default', 'Seed NotificationMessage 12', 'SEED-NOT-0012', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0013', 'default', 'Seed NotificationMessage 13', 'SEED-NOT-0013', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0014', 'default', 'Seed NotificationMessage 14', 'SEED-NOT-0014', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0015', 'default', 'Seed NotificationMessage 15', 'SEED-NOT-0015', 'DRAFT', 'PREMIUM', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0016', 'default', 'Seed NotificationMessage 16', 'SEED-NOT-0016', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0017', 'default', 'Seed NotificationMessage 17', 'SEED-NOT-0017', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0018', 'default', 'Seed NotificationMessage 18', 'SEED-NOT-0018', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0019', 'default', 'Seed NotificationMessage 19', 'SEED-NOT-0019', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0020', 'default', 'Seed NotificationMessage 20', 'SEED-NOT-0020', 'ACTIVE', 'PREMIUM', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0021', 'default', 'Seed NotificationMessage 21', 'SEED-NOT-0021', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0022', 'default', 'Seed NotificationMessage 22', 'SEED-NOT-0022', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0023', 'default', 'Seed NotificationMessage 23', 'SEED-NOT-0023', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0024', 'default', 'Seed NotificationMessage 24', 'SEED-NOT-0024', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0025', 'default', 'Seed NotificationMessage 25', 'SEED-NOT-0025', 'DRAFT', 'PREMIUM', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0026', 'default', 'Seed NotificationMessage 26', 'SEED-NOT-0026', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0027', 'default', 'Seed NotificationMessage 27', 'SEED-NOT-0027', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0028', 'default', 'Seed NotificationMessage 28', 'SEED-NOT-0028', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0029', 'default', 'Seed NotificationMessage 29', 'SEED-NOT-0029', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0030', 'default', 'Seed NotificationMessage 30', 'SEED-NOT-0030', 'ACTIVE', 'PREMIUM', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0031', 'default', 'Seed NotificationMessage 31', 'SEED-NOT-0031', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0032', 'default', 'Seed NotificationMessage 32', 'SEED-NOT-0032', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0033', 'default', 'Seed NotificationMessage 33', 'SEED-NOT-0033', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0034', 'default', 'Seed NotificationMessage 34', 'SEED-NOT-0034', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0035', 'default', 'Seed NotificationMessage 35', 'SEED-NOT-0035', 'DRAFT', 'PREMIUM', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0036', 'default', 'Seed NotificationMessage 36', 'SEED-NOT-0036', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0037', 'default', 'Seed NotificationMessage 37', 'SEED-NOT-0037', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0038', 'default', 'Seed NotificationMessage 38', 'SEED-NOT-0038', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0039', 'default', 'Seed NotificationMessage 39', 'SEED-NOT-0039', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0040', 'default', 'Seed NotificationMessage 40', 'SEED-NOT-0040', 'ACTIVE', 'PREMIUM', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0041', 'default', 'Seed NotificationMessage 41', 'SEED-NOT-0041', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0042', 'default', 'Seed NotificationMessage 42', 'SEED-NOT-0042', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0043', 'default', 'Seed NotificationMessage 43', 'SEED-NOT-0043', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0044', 'default', 'Seed NotificationMessage 44', 'SEED-NOT-0044', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0045', 'default', 'Seed NotificationMessage 45', 'SEED-NOT-0045', 'DRAFT', 'PREMIUM', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0046', 'default', 'Seed NotificationMessage 46', 'SEED-NOT-0046', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0047', 'default', 'Seed NotificationMessage 47', 'SEED-NOT-0047', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0048', 'default', 'Seed NotificationMessage 48', 'SEED-NOT-0048', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0049', 'default', 'Seed NotificationMessage 49', 'SEED-NOT-0049', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0050', 'default', 'Seed NotificationMessage 50', 'SEED-NOT-0050', 'ACTIVE', 'PREMIUM', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0051', 'default', 'Seed NotificationMessage 51', 'SEED-NOT-0051', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0052', 'default', 'Seed NotificationMessage 52', 'SEED-NOT-0052', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0053', 'default', 'Seed NotificationMessage 53', 'SEED-NOT-0053', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0054', 'default', 'Seed NotificationMessage 54', 'SEED-NOT-0054', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0055', 'default', 'Seed NotificationMessage 55', 'SEED-NOT-0055', 'DRAFT', 'PREMIUM', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0056', 'default', 'Seed NotificationMessage 56', 'SEED-NOT-0056', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0057', 'default', 'Seed NotificationMessage 57', 'SEED-NOT-0057', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0058', 'default', 'Seed NotificationMessage 58', 'SEED-NOT-0058', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO notification_messages (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-notification_service-0059', 'default', 'Seed NotificationMessage 59', 'SEED-NOT-0059', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded NotificationMessage item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;

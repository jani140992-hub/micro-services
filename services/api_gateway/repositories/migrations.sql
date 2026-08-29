-- =============================================================
-- PostgreSQL Migration Schema for API Gateway Service
-- Database Target: gateway_db
-- Version: 1.0.0 (Baseline)
-- =============================================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "btree_gist";

-- -------------------------------------------------------------
-- Table: gateway_routes (Primary Aggregate Table)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS gateway_routes (
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

CREATE INDEX IF NOT EXISTS idx_gateway_routes_tenant ON gateway_routes (tenant_id);
CREATE INDEX IF NOT EXISTS idx_gateway_routes_status ON gateway_routes (status);
CREATE INDEX IF NOT EXISTS idx_gateway_routes_category ON gateway_routes (category);
CREATE INDEX IF NOT EXISTS idx_gateway_routes_created_at ON gateway_routes (created_at DESC);
CREATE INDEX IF NOT EXISTS idx_gateway_routes_attributes_gin ON gateway_routes USING gin (attributes_json);

-- -------------------------------------------------------------
-- Table: gateway_routes_sub1 (Child Entity 1)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS gateway_routes_sub1 (
    id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid()::text,
    parent_id VARCHAR(36) NOT NULL REFERENCES gateway_routes(id) ON DELETE CASCADE,
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
CREATE INDEX IF NOT EXISTS idx_gateway_routes_sub1_parent ON gateway_routes_sub1 (parent_id);

-- -------------------------------------------------------------
-- Table: gateway_routes_sub2 (Child Entity 2)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS gateway_routes_sub2 (
    id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid()::text,
    parent_id VARCHAR(36) NOT NULL REFERENCES gateway_routes(id) ON DELETE CASCADE,
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
CREATE INDEX IF NOT EXISTS idx_gateway_routes_sub2_parent ON gateway_routes_sub2 (parent_id);

-- -------------------------------------------------------------
-- Table: gateway_routes_outbox (Transactional Outbox Pattern)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS gateway_routes_outbox (
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
CREATE INDEX IF NOT EXISTS idx_gateway_routes_outbox_status ON gateway_routes_outbox (status, created_at);

-- -------------------------------------------------------------
-- Data Seeding: Default Enterprise Seed Records
-- -------------------------------------------------------------
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0001', 'default', 'Seed GatewayRoute 1', 'SEED-API-0001', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0002', 'default', 'Seed GatewayRoute 2', 'SEED-API-0002', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0003', 'default', 'Seed GatewayRoute 3', 'SEED-API-0003', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0004', 'default', 'Seed GatewayRoute 4', 'SEED-API-0004', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0005', 'default', 'Seed GatewayRoute 5', 'SEED-API-0005', 'DRAFT', 'PREMIUM', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0006', 'default', 'Seed GatewayRoute 6', 'SEED-API-0006', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0007', 'default', 'Seed GatewayRoute 7', 'SEED-API-0007', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0008', 'default', 'Seed GatewayRoute 8', 'SEED-API-0008', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0009', 'default', 'Seed GatewayRoute 9', 'SEED-API-0009', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0010', 'default', 'Seed GatewayRoute 10', 'SEED-API-0010', 'ACTIVE', 'PREMIUM', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0011', 'default', 'Seed GatewayRoute 11', 'SEED-API-0011', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0012', 'default', 'Seed GatewayRoute 12', 'SEED-API-0012', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0013', 'default', 'Seed GatewayRoute 13', 'SEED-API-0013', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0014', 'default', 'Seed GatewayRoute 14', 'SEED-API-0014', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0015', 'default', 'Seed GatewayRoute 15', 'SEED-API-0015', 'DRAFT', 'PREMIUM', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0016', 'default', 'Seed GatewayRoute 16', 'SEED-API-0016', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0017', 'default', 'Seed GatewayRoute 17', 'SEED-API-0017', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0018', 'default', 'Seed GatewayRoute 18', 'SEED-API-0018', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0019', 'default', 'Seed GatewayRoute 19', 'SEED-API-0019', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0020', 'default', 'Seed GatewayRoute 20', 'SEED-API-0020', 'ACTIVE', 'PREMIUM', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0021', 'default', 'Seed GatewayRoute 21', 'SEED-API-0021', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0022', 'default', 'Seed GatewayRoute 22', 'SEED-API-0022', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0023', 'default', 'Seed GatewayRoute 23', 'SEED-API-0023', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0024', 'default', 'Seed GatewayRoute 24', 'SEED-API-0024', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0025', 'default', 'Seed GatewayRoute 25', 'SEED-API-0025', 'DRAFT', 'PREMIUM', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0026', 'default', 'Seed GatewayRoute 26', 'SEED-API-0026', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0027', 'default', 'Seed GatewayRoute 27', 'SEED-API-0027', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0028', 'default', 'Seed GatewayRoute 28', 'SEED-API-0028', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0029', 'default', 'Seed GatewayRoute 29', 'SEED-API-0029', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0030', 'default', 'Seed GatewayRoute 30', 'SEED-API-0030', 'ACTIVE', 'PREMIUM', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0031', 'default', 'Seed GatewayRoute 31', 'SEED-API-0031', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0032', 'default', 'Seed GatewayRoute 32', 'SEED-API-0032', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0033', 'default', 'Seed GatewayRoute 33', 'SEED-API-0033', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0034', 'default', 'Seed GatewayRoute 34', 'SEED-API-0034', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0035', 'default', 'Seed GatewayRoute 35', 'SEED-API-0035', 'DRAFT', 'PREMIUM', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0036', 'default', 'Seed GatewayRoute 36', 'SEED-API-0036', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0037', 'default', 'Seed GatewayRoute 37', 'SEED-API-0037', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0038', 'default', 'Seed GatewayRoute 38', 'SEED-API-0038', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0039', 'default', 'Seed GatewayRoute 39', 'SEED-API-0039', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0040', 'default', 'Seed GatewayRoute 40', 'SEED-API-0040', 'ACTIVE', 'PREMIUM', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0041', 'default', 'Seed GatewayRoute 41', 'SEED-API-0041', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0042', 'default', 'Seed GatewayRoute 42', 'SEED-API-0042', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0043', 'default', 'Seed GatewayRoute 43', 'SEED-API-0043', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0044', 'default', 'Seed GatewayRoute 44', 'SEED-API-0044', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0045', 'default', 'Seed GatewayRoute 45', 'SEED-API-0045', 'DRAFT', 'PREMIUM', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0046', 'default', 'Seed GatewayRoute 46', 'SEED-API-0046', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0047', 'default', 'Seed GatewayRoute 47', 'SEED-API-0047', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0048', 'default', 'Seed GatewayRoute 48', 'SEED-API-0048', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0049', 'default', 'Seed GatewayRoute 49', 'SEED-API-0049', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0050', 'default', 'Seed GatewayRoute 50', 'SEED-API-0050', 'ACTIVE', 'PREMIUM', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0051', 'default', 'Seed GatewayRoute 51', 'SEED-API-0051', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0052', 'default', 'Seed GatewayRoute 52', 'SEED-API-0052', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0053', 'default', 'Seed GatewayRoute 53', 'SEED-API-0053', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0054', 'default', 'Seed GatewayRoute 54', 'SEED-API-0054', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0055', 'default', 'Seed GatewayRoute 55', 'SEED-API-0055', 'DRAFT', 'PREMIUM', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0056', 'default', 'Seed GatewayRoute 56', 'SEED-API-0056', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0057', 'default', 'Seed GatewayRoute 57', 'SEED-API-0057', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0058', 'default', 'Seed GatewayRoute 58', 'SEED-API-0058', 'ACTIVE', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;
INSERT INTO gateway_routes (id, tenant_id, name, code, status, category, version, description) VALUES ('seed-api_gateway-0059', 'default', 'Seed GatewayRoute 59', 'SEED-API-0059', 'DRAFT', 'STANDARD', 1, 'Enterprise seeded GatewayRoute item for automated integration tests and demonstration') ON CONFLICT (code) DO NOTHING;

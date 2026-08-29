# CloudMart Distributed Platform - Data Dictionary

| Service | Primary Table | Key Fields | Storage Engine | Isolation Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **API Gateway** | `gateway_routes` | `id`, `code`, `name`, `status` | Redis / Memory | Edge routing table |
| **Identity Service** | `user_credentials` | `id`, `code`, `status`, `version` | PostgreSQL (`identity_db`) | Database-per-service |
| **User Service** | `user_profiles` | `id`, `code`, `status`, `version` | PostgreSQL (`user_db`) | Database-per-service |
| **Catalog Service** | `product_items` | `id`, `code`, `category`, `status` | PostgreSQL (`catalog_db`) | Database-per-service |
| **Inventory Service** | `stock_items` | `id`, `code`, `category`, `status` | PostgreSQL (`inventory_db`)| Database-per-service |
| **Order Service** | `customer_orders` | `id`, `code`, `status`, `version` | PostgreSQL (`order_db`) | Database-per-service |
| **Payment Service** | `payment_transactions` | `id`, `code`, `status`, `version` | PostgreSQL (`payment_db`)| Database-per-service |
| **Shipping Service** | `shipment_consignments`| `id`, `code`, `category`, `status` | PostgreSQL (`shipping_db`)| Database-per-service |
| **Notification Service**| `notification_messages`| `id`, `code`, `status`, `version` | PostgreSQL (`notification_db`)| Database-per-service |
| **Analytics Service** | `stream_metric_records`| `id`, `code`, `category`, `status` | PostgreSQL (`analytics_db`)| Database-per-service |

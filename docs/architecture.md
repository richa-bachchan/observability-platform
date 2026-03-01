# Architecture Overview

This platform implements a production-style Kubernetes observability stack deployed on AWS EKS.

## Components

### Infrastructure
- AWS EKS cluster provisioned via Terraform
- Remote Terraform state stored in S3
- State locking via DynamoDB

### Application Layer
- Frontend service (Flask)
- Backend service (Flask)
- 5% error simulation for SLO testing

### Observability Stack
- Prometheus (metrics)
- Loki (logs)
- Tempo (traces)
- OpenTelemetry Collector
- Grafana (visualization)

## Data Flow

1. Frontend calls Backend
2. Backend generates:
   - Metrics (Prometheus format)
   - Logs
   - Traces (OTLP)
3. OpenTelemetry Collector:
   - Sends traces to Tempo
   - Exposes metrics to Prometheus
   - Sends logs to Loki
4. Grafana visualizes all three signals

## Key Features

- Distributed tracing
- Error rate monitoring
- Declarative Kubernetes manifests
- Clean GitOps-ready structure

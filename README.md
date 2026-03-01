## Architecture

```mermaid
flowchart TB

  subgraph Applications
    FE[Frontend Service]
    BE[Backend Service]
  end

  subgraph Observability
    OTEL[OpenTelemetry Collector]
    PROM[Prometheus]
    LOKI[Loki]
    TEMPO[Tempo]
    GRAF[Grafana]
  end

  subgraph AWS_Infrastructure
    EKS[EKS Cluster]
    S3[S3 - Terraform State]
    DDB[DynamoDB - State Lock]
  end

  FE -->|HTTP| BE
  FE -->|Traces| OTEL
  BE -->|Traces| OTEL
  BE -->|Metrics| PROM
  BE -->|Logs| LOKI

  OTEL -->|Traces| TEMPO
  PROM --> GRAF
  LOKI --> GRAF
  TEMPO --> GRAF

  EKS --> FE
  EKS --> BE
  EKS --> OTEL
  EKS --> PROM
  EKS --> LOKI
  EKS --> TEMPO

  S3 --> EKS
  DDB --> EKS

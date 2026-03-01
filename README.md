## Architecture (Layered View)

```mermaid
flowchart TB

%% Application Layer
subgraph Application Layer
  FE[Frontend Service]
  BE[Backend Service]
end

%% Telemetry Layer
subgraph Telemetry Pipeline
  OTEL[OpenTelemetry Collector]
end

%% Observability Layer
subgraph Observability Stack
  PROM[Prometheus - Metrics]
  LOKI[Loki - Logs]
  TEMPO[Tempo - Traces]
  GRAF[Grafana - Visualization]
end

%% Infrastructure Layer
subgraph Infrastructure
  EKS[EKS Cluster]
  S3[S3 - Terraform State]
  DDB[DynamoDB - State Lock]
end

%% Application Flow
FE --> BE

%% Telemetry Flow
FE -->|Traces| OTEL
BE -->|Traces| OTEL
BE -->|Metrics| PROM
BE -->|Logs| LOKI

OTEL -->|Traces| TEMPO

%% Visualization
PROM --> GRAF
LOKI --> GRAF
TEMPO --> GRAF

%% Infrastructure Hosting
EKS --> FE
EKS --> BE
EKS --> OTEL
EKS --> PROM
EKS --> LOKI
EKS --> TEMPO

S3 --> EKS
DDB --> EKS

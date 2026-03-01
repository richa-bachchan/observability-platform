# Logging Layer (Loki)

## Purpose
Centralized log aggregation for Kubernetes workloads.

## Components
- Loki (log storage)
- Promtail (log collector, if used)

## Flow
Application logs → Promtail → Loki → Grafana

## Kubernetes Resources
- Deployment
- Service
- ConfigMap

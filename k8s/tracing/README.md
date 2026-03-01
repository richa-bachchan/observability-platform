# Tracing Layer (Tempo)

## Purpose
Stores and indexes distributed traces.

## Flow
Application → OpenTelemetry Collector → Tempo → Grafana

## Features
- Distributed tracing across frontend and backend
- Trace visualization in Grafana

## Kubernetes Resources
- Deployment
- Service
- ConfigMap

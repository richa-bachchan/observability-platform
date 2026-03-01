# OpenTelemetry Collector

## Purpose
Central telemetry pipeline for logs, metrics, and traces.

## Responsibilities
- Receives OTLP traces and metrics
- Exports traces to Tempo
- Exposes metrics to Prometheus
- Sends logs to Loki

## Image
Uses `otel/opentelemetry-collector-contrib` to support Loki exporter.

## Kubernetes Resources
- ConfigMap (collector configuration)
- Deployment

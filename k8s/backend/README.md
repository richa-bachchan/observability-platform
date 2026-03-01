# Backend Service

## Overview
Flask-based backend application deployed on Kubernetes.

## Responsibilities
- Handles API requests from frontend
- Generates Prometheus metrics
- Emits distributed traces via OpenTelemetry
- Simulates 5% error rate for SLO testing

## Observability
- Metrics exposed at `/metrics`
- Scraped by Prometheus via ServiceMonitor
- Traces sent to OpenTelemetry Collector
- Logs aggregated by Loki

## Kubernetes Resources
- Deployment
- Service

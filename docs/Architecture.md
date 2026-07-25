# StockAI Architecture

## Overview

StockAI is a modular investment analysis platform that downloads market data,
stores historical prices, calculates technical indicators, scores investment
opportunities, and presents insights through dashboards and AI-generated
summaries.

## High-Level Architecture
             Market Data Providers
                      │
                      ▼
             Market Data Client
                      │
                      ▼
              Price Downloader
                      │
                      ▼
                SQLite Database
                      │
     ┌────────────────┼────────────────┐
     ▼                ▼                ▼


## Layers

### Presentation Layer
- Dashboard
- Reports
- Alerts

### Service Layer
- Downloader
- Indicator Engine
- Scoring Engine

### Repository Layer
- Database access
- CRUD operations

### Infrastructure Layer
- SQLite
- Logging
- Configuration
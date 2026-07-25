# Database Design

## Current Database

SQLite

## Planned Tables

### stock_prices

Daily historical prices.

### company_profiles

Fundamental company information.

### technical_indicators

Calculated indicators.

### investment_scores

Daily investment scores.

### alerts

Generated alerts.

## Design Principles

- Historical data is never overwritten.
- One record per ticker per trading day.
- Use repositories instead of raw SQL in application code.
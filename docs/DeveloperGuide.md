# Developer Guide

## Development Workflow

1. Pull latest changes.
2. Create a feature branch.
3. Implement one feature.
4. Add tests.
5. Run formatting.
6. Run linting.
7. Commit changes.
8. Merge after testing.

## Running the Project

```bash
python -m stockai.main
```

## Running Tests

```bash
pytest
```

## Formatting

```bash
black src tests
```

## Linting

```bash
ruff check src tests
```

## Folder Responsibilities

| Folder | Responsibility |
|---------|----------------|
| downloader | Download market data |
| market_data | External API clients |
| repository | Database access |
| indicators | Technical indicators |
| scoring | Investment score calculation |
| dashboard | Streamlit UI |
| alerts | Email and Telegram |
| ai | AI-powered summaries |
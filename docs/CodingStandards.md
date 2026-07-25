# Coding Standards

## General

- Use Python 3.12+
- Follow PEP 8
- Format with Black
- Lint with Ruff

## Naming

Classes

```python
PriceDownloader
```

Functions

```python
download_prices()
```

Variables

```python
current_price
```

Constants

```python
MAX_RETRIES = 3
```

## Imports

1. Standard library
2. Third-party packages
3. Local imports

## Logging

Always use Loguru.

Never use:

```python
print(...)
```

Instead:

```python
logger.info(...)
```

## Error Handling

Catch expected exceptions.

Never use bare:

```python
except:
```

Always log the error.
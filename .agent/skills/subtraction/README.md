# Subtraction Skill

A simple, reusable agent skill that calculates the difference between two numbers.

## Features

- Accepts two numeric inputs (`a` and `b`).
- Returns the mathematical difference (`a - b`).
- Compatible with class-based and functional agent frameworks.

## Input Parameters

The skill accepts a JSON payload with the following parameters:

| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| `a`       | number | Yes      | The first number (minuend). |
| `b`       | number | Yes      | The second number to subtract (subtrahend). |

## Example Usage

### JSON Input
```json
{
  "a": 50,
  "b": 18
}
```

### JSON Output
```json
32.0
```

### Python Programmatic Usage
```python
from skill import execute

result = execute(50, 18)
print(result) # Output: 32.0
```

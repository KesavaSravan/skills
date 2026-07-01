# Addition Skill

A simple, reusable agent skill that calculates the sum of two numbers.

## Features

- Accepts two numeric inputs (`a` and `b`).
- Returns the mathematical sum (`a + b`).
- Compatible with class-based and functional agent frameworks.

## Input Parameters

The skill accepts a JSON payload with the following parameters:

| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| `a`       | number | Yes      | The first number to add. |
| `b`       | number | Yes      | The second number to add. |

## Example Usage

### JSON Input
```json
{
  "a": 15,
  "b": 27
}
```

### JSON Output
```json
42.0
```

### Python Programmatic Usage
```python
from skill import execute

result = execute(15, 27)
print(result) # Output: 42.0
```

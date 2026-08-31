# AI-Assisted Debugging Record

## Issue selected for debugging

During development, the storage layer was treated as trusted input. A malformed `expenses.json` file could cause `json.load()` to raise `JSONDecodeError` and terminate the application.

### Problematic approach

```python
with DATA_FILE.open("r", encoding="utf-8") as file:
    return json.load(file)
```

If the JSON file was manually edited or became corrupted, the program could crash before showing the menu.

## AI debugging approach

The AI was asked to review the storage code, identify the failure mode, explain the exception, and suggest a minimal fix.

### Improvement applied

The final implementation catches:
- `json.JSONDecodeError`
- `OSError`
- `ValueError`

It prints a warning and safely starts with an empty list.

## Verification

An automated test named `test_load_invalid_json_returns_empty_list` creates invalid JSON and verifies that the application returns an empty list instead of crashing.

This demonstrates the Week 5 workflow of **identify → fix → test → verify**.

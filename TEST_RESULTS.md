# Test Results

The project uses Python's built-in `unittest` framework.

Run:

```bash
python -m unittest -v test_expense_tracker.py
```

Expected result:

```text
Ran 10 tests
OK
```

The test suite covers:

| Test | Purpose |
|---|---|
| validate positive amount | Valid numeric input |
| reject zero amount | Boundary validation |
| reject text amount | Type/input validation |
| clean category | Input normalization |
| reject empty category | Required-field validation |
| add expense | Core application behavior |
| calculate total | Calculation correctness |
| category totals | Grouped calculation |
| save/load | Persistence |
| invalid JSON | Error handling |

All 10 tests are designed to pass against the final implementation.

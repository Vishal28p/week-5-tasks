# Personal Expense Tracker

## Week 5 – Gen AI Internship

A small command-line Python application created for the Week 5 task on **AI for Programming & Development**.

The project demonstrates an AI-assisted development workflow:

**Plan → Code → Review → Debug → Test → Improve**

## Features

- Add an expense
- Validate amount, category, and description
- Store expenses locally in `expenses.json`
- View all expenses
- Calculate total spending
- View category-wise spending
- Handle invalid input and corrupted JSON data
- Automated unit tests using Python's built-in `unittest`

## Requirements

- Python 3.9 or later
- No third-party packages are required.

## Run the application

```bash
python expense_tracker.py
```

The application creates `expenses.json` when an expense is saved.

## Run the tests

```bash
python -m unittest -v test_expense_tracker.py
```

## Example workflow

1. Select `1` to add an expense.
2. Enter an amount such as `250.50`.
3. Enter a category such as `Food`.
4. Enter a description such as `Lunch`.
5. Select `2` to view expenses.
6. Select `3` to view the spending summary.
7. Select `4` to exit.

## Error handling and validation

The application rejects:
- Non-numeric amounts
- Zero or negative amounts
- Empty categories
- Categories longer than 30 characters
- Empty descriptions
- Descriptions longer than 100 characters
- Invalid/corrupted JSON storage

## Project structure

```text
expense_tracker_week5/
├── expense_tracker.py
├── test_expense_tracker.py
├── expenses.json
├── README.md
├── AI_PROMPTS.md
├── CODE_REVIEW.md
├── BUG_DEBUGGING.md
├── TEST_RESULTS.md
└── WEEK5_REPORT.pdf
```

## AI usage

AI was used as a development assistant for:
- Breaking requirements into functions
- Generating an initial implementation
- Explaining unfamiliar Python concepts
- Reviewing and debugging code
- Suggesting validation and error handling
- Generating test cases
- Drafting documentation

All generated suggestions were reviewed and verified before being included.

## Manual review

The final code was manually reviewed for:
- Input validation
- Exception handling
- File handling
- Readability
- Function separation
- Test coverage
- Security considerations

No passwords, API keys, or other sensitive information are used.

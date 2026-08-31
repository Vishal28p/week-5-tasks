import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import expense_tracker


class ExpenseTrackerTests(unittest.TestCase):

    def test_validate_amount_accepts_positive_number(self):
        self.assertEqual(expense_tracker.validate_amount("125.50"), 125.50)

    def test_validate_amount_rejects_zero(self):
        with self.assertRaises(ValueError):
            expense_tracker.validate_amount("0")

    def test_validate_amount_rejects_text(self):
        with self.assertRaises(ValueError):
            expense_tracker.validate_amount("abc")

    def test_validate_category_cleans_text(self):
        self.assertEqual(expense_tracker.validate_category("  food  "), "Food")

    def test_validate_category_rejects_empty(self):
        with self.assertRaises(ValueError):
            expense_tracker.validate_category("   ")

    def test_add_expense_creates_record(self):
        expenses = []
        record = expense_tracker.add_expense(
            expenses, "250", "food", "Lunch"
        )
        self.assertEqual(len(expenses), 1)
        self.assertEqual(record["amount"], 250.00)
        self.assertEqual(record["category"], "Food")
        self.assertEqual(record["description"], "Lunch")

    def test_calculate_total(self):
        expenses = [
            {"amount": 100.00},
            {"amount": 250.50},
        ]
        self.assertEqual(expense_tracker.calculate_total(expenses), 350.50)

    def test_category_totals(self):
        expenses = [
            {"amount": 100.00, "category": "Food"},
            {"amount": 50.00, "category": "Travel"},
            {"amount": 25.00, "category": "Food"},
        ]
        self.assertEqual(
            expense_tracker.category_totals(expenses),
            {"Food": 125.00, "Travel": 50.00},
        )

    def test_save_and_load_expenses(self):
        expenses = [
            {
                "id": 1,
                "date": "2026-08-31",
                "amount": 99.99,
                "category": "Books",
                "description": "Python book",
            }
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = Path(temp_dir) / "expenses.json"
            with patch.object(expense_tracker, "DATA_FILE", temp_file):
                self.assertTrue(expense_tracker.save_expenses(expenses))
                self.assertEqual(expense_tracker.load_expenses(), expenses)

    def test_load_invalid_json_returns_empty_list(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = Path(temp_dir) / "expenses.json"
            temp_file.write_text("{invalid json", encoding="utf-8")

            with patch.object(expense_tracker, "DATA_FILE", temp_file):
                with patch("builtins.print"):
                    self.assertEqual(expense_tracker.load_expenses(), [])


if __name__ == "__main__":
    unittest.main()

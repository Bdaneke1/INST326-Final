import unittest
import Finance_Tracker

class TestFinanceMethods(unittest.TestCase):
    def test_add_income(self):
        finances = Finance_Tracker.Finances()
        finances.add_income("Work Salary", 2000, "2024-05-01")
        self.assertTrue(any(transaction['source'] == "Work Salary" for transaction in finances.income))

    def test_add_expense(self):
        finances = Finance_Tracker.Finances()
        finances.add_expense("Rent", 1000, "2024-05-05")
        self.assertTrue(any(transaction['category'] == "Rent" for transaction in finances.expenses))

    def test_add_transaction(self):
        finances = Finance_Tracker.Finances()
        finances.add_transaction("2024-05-10", "Expense", 50, "Groceries")
        self.assertTrue(any(transaction['description'] == "Groceries" for transaction in finances.transactions))

    def test_add_investment(self):
        investments = Finance_Tracker.Investments("My Portfolio")
        investments.add_investment("Stocks", 5000)
        self.assertIn("Stocks", investments.investments)

    def test_remove_investment(self):
        investments = Finance_Tracker.Investments("My Portfolio")
        investments.add_investment("Stocks", 5000)
        investments.remove_investment("Stocks")
        self.assertNotIn("Stocks", investments.investments)

    def test_calculate_investment_growth(self):
        investments = Finance_Tracker.Investments("My Portfolio")
        investments.add_investment("Stocks", 5000)
        investments.calculate_investment_growth("Stocks", 0.05)
        self.assertEqual(investments.investments["Stocks"], 5250)

    def test_convert_currency(self):
        converted_amount = Finance_Tracker.convert_currency(100, "USD", "EUR")
        self.assertIsNotNone(converted_amount)

    def test_build_report(self):
        finances = Finance_Tracker.Finances()
        finances.add_income("Work Salary", 2000, "2024-05-01")
        finances.add_expense("Rent", 1000, "2024-05-05")
        finances.add_transaction("2024-05-10", "Expense", 50, "Groceries")
        report = finances.build_report("2024-05-01", "2024-05-10")
        self.assertEqual(len(report['Income']), 1)
        self.assertEqual(len(report['Expenses']), 1)
        self.assertEqual(len(report['Transactions']), 1)

if __name__ == '__main__':
    unittest.main()

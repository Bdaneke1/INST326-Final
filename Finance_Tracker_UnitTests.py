import unittest
import finance_tracker

class TestFinanceMethods(unittest.TestCase):
    def setUp(self):
        """Setup for each test case; ensures each test is independent."""
        self.finances = finance_tracker.Finances()
        self.investments = finance_tracker.Investments("My Portfolio")

    def test_add_income(self):
        """Test adding income and validate all properties."""
        self.finances.add_income("Work Salary", 2000, "2024-05-01")
        expected = {'source': "Work Salary", 'amount': 2000, 'date': "2024-05-01"}
        self.assertIn(expected, self.finances.income)
        self.assertEqual(len(self.finances.income), 1)  # Ensure only one record is added

    def test_add_expense(self):
        """Test adding expenses and check for correct insertion."""
        self.finances.add_expense("Rent", 1000, "2024-05-05")
        expected = {'category': "Rent", 'amount': 1000, 'date': "2024-05-05"}
        self.assertIn(expected, self.finances.expenses)
        self.assertEqual(len(self.finances.expenses), 1)  # Confirm one entry is present

    def test_add_transaction(self):
        """Ensure transactions are added correctly with all details."""
        self.finances.add_transaction("2024-05-10", "Expense", 50, "Groceries")
        expected = {'date': "2024-05-10", 'category': "Expense", 'amount': 50, 'description': "Groceries"}
        self.assertIn(expected, self.finances.transactions)
        self.assertEqual(self.finances.transactions[0]['amount'], 50)  # Verify amount

    def test_add_investment(self):
        """Test investment addition and assert correctness of the update."""
        self.investments.add_investment("Stocks", 5000)
        self.assertEqual(self.investments.investments.get("Stocks"), 5000)

    def test_remove_investment(self):
        """Check correct investment removal functionality."""
        self.investments.add_investment("Stocks", 5000)
        self.investments.remove_investment("Stocks")
        self.assertNotIn("Stocks", self.investments.investments)

    def test_calculate_investment_growth(self):
        """Test the calculation of investment growth."""
        self.investments.add_investment("Stocks", 5000)
        self.investments.calculate_investment_growth("Stocks", 0.10)  # 10% growth
        self.assertEqual(self.investments.investments["Stocks"], 5500)

    def test_build_report(self):
        """Verify that reports are generated correctly with accurate data."""
        self.finances.add_income("Work Salary", 2000, "2024-05-01")
        self.finances.add_expense("Rent", 1000, "2024-05-05")
        self.finances.add_transaction("2024-05-10", "Expense", 50, "Groceries")
        report = self.finances.build_report("2024-05-01", "2024-05-10")
        self.assertEqual(report['Income'][0], {'source': 'Work Salary', 'amount': 2000, 'date': '2024-05-01'})
        self.assertEqual(report['Expenses'][0], {'category': 'Rent', 'amount': 1000, 'date': '2024-05-05'})
        self.assertEqual(report['Transactions'][0], {'date': '2024-05-10', 'category': 'Expense', 'amount': 50, 'description': 'Groceries'})

if __name__ == '__main__':
    unittest.main()

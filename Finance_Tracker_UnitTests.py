import unittest
import Finance_Tracker

class TestFinanceMethods(unittest.TestCase):
    def test_add_income(self):
        finances = Finance_Tracker.Finances()
        finances.add_income_source("Work Salary")
        self.assertIn("Work Salary", finances.income)
     

    def test_add_expense(self):
        finances = Finance_Tracker.Finances()
        finances.add_expense_category("Fixed and Variable Costs")
        self.assertIn("Fixed and Variable Costs", finances.expenses)
      

    def test_add_savings(self):
        finances = Finance_Tracker.Finances()
        finances.add_savings_category("Savings Account")
        self.assertIn("Savings Accounts", finances.savings)
     
    def test_transaction(self):
        transaction = Finance_Tracker.Transaction("2024-04-23", "Expense", 500, "Rent")
        self.assertEqual(transaction.date, "2024-04-23")
        self.assertEqual(transaction.category, "Expense")
        self.assertEqual(transaction.amount, 500)
        self.assertEqual(transaction.description, "Rent")

    def test_investment_add_remove(self):
        investments = Finance_Tracker.Investments("Portfolio")
        investments.add_investment("Stocks", 5000)
        self.assertIn("Stocks", investments.investments)
        investments.remove_investment("Stocks")
        self.assertNotIn("Stocks", investments.investments)

if __name__ == '__main__':
    unittest.main()
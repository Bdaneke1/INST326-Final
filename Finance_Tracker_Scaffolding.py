"""
Basic Outline for the financial management system.
"""

class Finances:
    """
    Creates a class that holds the user's financial data.
    """
    
    def __init__(self):
        """
        Initializes user's finances
        
        Args:
            income: list of income sources
            expenses: list of expenses
            savings: list of different investments/savings accounts, etc.
        """
        self.income = []
        self.expenses = []
        self.savings = []
        
    def add_income_source(self, source):
        """
        Adds a new income source to the system
        
        Args:
            source (str): represents the name of the income source(job, etc.)
        """
        self.income.append(source)
        
    def add_expense_category(self, category):
        """
        Adds a new expense category to the system
        
        Args:
            category (str): represents the name of the expense category
        """
        self.expenses.append(category)
        
    def add_savings_category(self, category): #may not be needed because of the investments class
        """
        Adds a new savings category to the system
        
        Args:
            category (str): represents the name of the savings category
        """
        self.savings.append(category)
        
    def build_report(self, start_date, end_date):
        """
        Generates a report for the specified start and end dates
        
        Args:
            start_date (str): start date of reporting period
            end_date (str): end date of reporting period
        """
        report = {}
        report['Income'] = = [inc for inc in self.income if start_date <= inc['date'] <= end_date]
        report['Expenses'] = [exp for exp in self.expenses if start_date <= exp['date'] <= end_date]
        report['Savings'] = [sav for sav in self.savings if start_date <= sav['date'] <= end_date]
        return report


    #If we use a JSON for the data, this is how we would save the data to a JSON file
    def save_to_file(self, file_name):
        with open(file_name, 'w') as file:
            json.dump({'income': self.income, 'expenses': self.expenses, 'savings': self.savings}, file)

    #If we use a JSON for the finanical data, this will ead it and update the clases 
    def load_from_file(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
            self.income = data['income']
            self.expenses = data['expenses']
            self.savings = data['savings']

class Transaction:
    """
    Represents each financial transaction the user makes.
    """
    
    def __init__(self, date, category, amount, description):
        """
        Initializes each transaction with descriptors
        
        Args:
            date (str): date of the transaction
            category (str): income or expense or savings
            amount (int): monetary amount of the transaction
            description (str): description of the transaction
        """
        
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description
        
    #add formatting function and potentially more to organize transactions
    
class Investments:
    """
    Represents the user's financial portfolio
    """
    
    def __init__(self, name):
        """
        Initializes the portfolio with an empty list and name
        
        Args:
            name (str): name of the portfolio
        """
        self.name = name
        self.investments = {} 
        
    def add_investment(self, asset, amount):
        """
        Adds a new asset/investment to the portfolio
        
        Args:
            asset (str): name of the asset
            amount (int): monetary cost of the asset
        """
        self.investments[asset] = amount
        
    def remove_investment(self, asset):
        """
        Removes an asset/investment from the portfolio
        
        ArgS:
            asset (str): name of the asset that's being removed
        """
        if asset in self.investments:
            del self.investments[asset]
            
import unittest

class TestFinanceMethods(unittest.TestCase):
    def test_add_income(self):
        finances = Finances()
        finances.add_income_source("Work Salary")
        self.assertIN("Work Salary", finances.income)
     

    def test_add_expense(self):
        finances = Finances()
        finances.add_expense_category("Fixed and Variable Costs")
        self.assertIn("Fixed and Variable Costs", finances.expenses)
      

    def test_add_savings(self):
        finances = Finances()
        finances.add_savings_category("Savings Account")
        self.assertIN("Savings Accounts", finances.savings)
     
    def test_transaction(self):
        transaction = Transaction("2024-04-23", "Expense", 500, "Rent")
        self.assertEqual(transaction.date, "2024-04-23")
        self.assertEqual(transaction.category, "Expense")
        self.assertEqual(transaction.amount, 500)
        self.assertEqual(transaction.description, "Rent")

    def test_investment_add_remove(self):
        investments = Investments("Portfolio")
        investments.add_investment("Stocks", 5000)
        self.assertIn("Stocks", investments.investments)
        investments.remove_investment("Stocks")
        self.assertNotIn("Stocks", investments.investments)

if __name__ == '__main__':
    unittest.main()

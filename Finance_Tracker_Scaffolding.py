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
        #however we build the financial report
        
    #add save/load from file functions

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
        self.investments = [] #idk whether dictionary or list would be better for this
        
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
     

    def test_add_expense(self):
        finances = Finances()
      

    def test_add_savings(self):
        finances = Finances()
     
    def test_transaction(self):
       

    def test_investment_add_remove(self):
        

if __name__ == '__main__':
    unittest.main()

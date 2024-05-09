import json
import sys
import requests

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
        self.transactions = []
        
    def add_income_source(self, source):
        """
        Adds a new income source to the system
        
        Args:
            source (str): represents the name of the income source(job, etc.)
        """
        self.income.append(source)
        
    def update_income_source(self, old_source, new_source):
        """
        Allows user to update existing income source
        
        Args:
            old_source (str): existing income source
            new_source (str): replacement income source
        """
        try:
            index = self.income.index(old_source)
            self.income[index] = new_source
        except ValueError:
            print("Income source not found.")
            
    def add_expense_category(self, category):
        """
        Adds a new expense category to the system
        
        Args:
            category (str): represents the name of the expense category
        """
        self.expenses.append(category)

    def update_expense_category(self, old_category, new_category):
        """
        Allows user to update the expense category
        
        Args:
            old_category (str): existing expense category
            new_category (str): replacement expense category
        """
        try:
            index = self.expenses.index(old_category)
            self.expenses[index] = new_category
        except ValueError:
            print("Expense category not found.")
            
    def add_transaction(self, transaction):
        """
        Adds a new transaction to list
        
        Args:
            transaction: the transaction to add
        """
        self.transactions.append(transaction)
        
    def build_report(self, start_date, end_date):
        """
        Generates a report for the specified start and end dates
        
        Args:
            start_date (str): start date of reporting period
            end_date (str): end date of reporting period
        """
        report = {
            'Income': [inc for inc in self.income if start_date <= inc.date <= end_date],
            'Expenses': [exp for exp in self.expenses if start_date <= exp.date <= end_date],
            'Transactions': [trans for trans in self.transactions if start_date <= trans.date <= end_date]
        }
        
        return report

    #If we use a JSON for the data, this is how we would save the data to a JSON file
    def save_to_file(self, file_name):
        with open(file_name, 'w') as file:
            json.dump({'income': self.income, 'expenses': self.expenses}, file)

    #If we use a JSON for the finanical data, this will read it and update the clases 
    def load_from_file(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
            self.income = data['income']
            self.expenses = data['expenses']

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

    def calculate_investment_growth(self, asset, growth_rate):
        if asset in self.investments:
            return self.investments[asset] * (1 + growth_rate)
        else:
            print("Investment not found.")
            return None

class CurrencyNotFoundError(Exception):
    """Custom exception for indicating that the currency code was not found."""

def convert_currency(amount, from_currency, to_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()

        #checks if from_currency and to_currency exists in the exchange rates data
        if from_currency not in data['rates']:
            raise CurrencyNotFoundError(f"Currency code '{from_currency}' not found. Please use a valid currency code.")

        rates = data['rates']

        if to_currency not in rates:
            raise CurrencyNotFoundError(f"Currency code '{to_currency}' not found. Please use a valid currency code.")

        return amount * rates[to_currency]
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    except CurrencyNotFoundError as e:
        print(f"Error: {e}")
        return None

def main():
    print("Welcome to your Financial Management System!")
    
    finances = Finances()
    investments = Investments("My Portfolio")
    
    while True:
        print("\nOptions:")
        print("1. Add Income Source")
        print("2. Add Expense Category")
        print("3. Add Transaction")
        print("4. Add Investment")
        print("5. Generate Report")
        print("6. Save Data to JSON")
        print("7. Load Data from JSON")
        print("8. Convert Currency")
        print("9. View Income Sources")
        print("10. View Expense Categories")
        print("11. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            source = input("Enter the name of the income source: ")
            finances.add_income_source(source)
            print("Income source added successfully.")
        elif choice == '2':
            category = input("Enter the name of the expense category: ")
            finances.add_expense_category(category)
            print("Expense category added successfully.")
        elif choice == '3':
            date = input("Enter the date of the transaction (YYYY-MM-DD): ")
            category = input("Enter the category of the transaction (income/expense/savings): ")
            amount = float(input("Enter the amount of the transaction: "))
            description = input("Enter a description of the transaction: ")
            transaction = Transaction(date, category, amount, description)
            finances.add_transaction(transaction)
            print("Transaction added successfully.")
        elif choice == '4':
            asset = input("Enter the name of the asset: ")
            amount = float(input("Enter the amount of the investment: "))
            investments.add_investment(asset, amount)
            print("Investment added successfully.")
        elif choice == '5':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            report = finances.build_report(start_date, end_date)
            print("Report:")
            print(report)
        elif choice == '6':
            file_name = input("Enter the file name to save data to: ")
            finances.save_to_file(file_name)
            print("Data saved successfully.")
        elif choice == '7':
            file_name = input("Enter the file name to load data from: ")
            finances.load_from_file(file_name)
            print("Data loaded successfully.")
        elif choice == '8':
            amount = float(input("Enter the amount to convert: "))
            from_currency = input("Enter the source currency: ")
            to_currency = input("Enter the target currency: ")
            converted_amount = convert_currency(amount, from_currency, to_currency)
            print(f"Converted amount: {converted_amount} {to_currency}")
        elif choice == '9':
            print("Income Sources:")
            for source in finances.income:
                print(source)
        elif choice == '10':
            print("Expense Categories:")
            for category in finances.expenses:
                print(category)
        elif choice == '11':
            print("Exiting Financial Management System.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

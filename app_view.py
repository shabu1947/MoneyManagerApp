

from lib_money_manager import data_base
from lib_money_manager import money_calculator


class AppFunction:
    """
    This class serves as interface to app and libs
    """

    def __init__(self):
        self.categories = self.get_categories()
        self.accounts = ['Savings', 'CreditCard', 'Gift', 'Loan', 'Lend']
        self.spend_type = ['Cash', 'DebitCard', 'CreditCard']

    def __str__(self):
        return "My Manager GUI"

    def money_spent(self, amount, category_type, remarks=None, date=None, account='savings'):
        pass

    def display_total_expenditure_on(self, date):
        pass

    def display_total_expenditure_from_to(self, start_date, end_date):

        pass

    def display_category_wise_spends_on_date(self, date='Today'):
        pass

    def add_new_category(self):
        pass

    def read_category(self):
        pass

    def get_categories(self):
        # TODO Read categories from DB and return the list
        categories = ['Food', 'Movies', 'Travel', 'Rent', 'Bills', 'Others']
        return categories
        pass


class AppCall:

    def __init__(self):
        pass

    def view(self):
        pass
    pass

class CreditCard:
    """consumer cc"""

    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    # all getters
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._acnt
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        # check if sufficient funds
        if self.get_balance() + price <= price:
            self._balance += price
            return True
        else:
            return False
        
    def make_payment(self, amount):
        if amount > 0:
            self._balance -= amount
            return True
        else:
            return False

import logging
import random
from datetime import datetime

logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')

def generate_transaction_id():
    return f"TXN{random.randint(100000,999999)}"

class TransactionNotFoundError(Exception):
    pass
class AccountNotFoundError(Exception):
    pass
class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self,account_id,account_type,bal):
        self.account_id=account_id
        self.account_type=account_type
        self.bal=bal
        
        
    def deposit(self,amount):
        self.bal+=amount
        txn_id=generate_transaction_id()
        logging.info(f"Deposited{amount}into account. New balance is{self.bal}")
        return self.bal,txn_id

        
    def withdraw(self,amount):
        if amount<self.bal:
            raise InsufficientFundsError("Balance is less than the amount to be withdrawn!")
        else:
            self.bal-=amount
            txn_id=generate_transaction_id()
            logging.info(f"Withdrew{amount}from account. New balance is {self.bal}")
            return self.bal,txn_id

class Transaction:
    def __init__(self,transaction_id,account_id,txn_type,amount):
        self.transaction_id=transaction_id
        self.account_id=account_id
        self.txn_type=txn_type
        self.amount=amount
        self.timestamp=datetime.now()
        
    def get_transaction_info(self):
        return f"Transaction ID:{self.transaction_id}, Account ID:{self.account_id},Transaction type:{self.txn_type},Amount:{self.amount},time:{self.timestamp}"
    
    
class TransactionManager:
    def __init__(self):
        self.transactions={}
        self.accounts={}
        
    def create_account(self):
        account_id = input("Enter account ID: ")
        account_type = input("Enter account type: ")
        bal = float(input("Enter initial balance: "))

        self.accounts[account_id] = Account(account_id, account_type, bal)
        print("Account created successfully!")
            
    def initialize_transaction(self,account_id):
        pass
                
                
            
            
    def display_transactions(self):
        for key,val in self.transactions.items():
            return f"Transaction_ID:{key},Timestamp:{val}"
        
    

    
if __name__=="__main__":
    
    while True:
        print("Pick an action")
        print("1.Initialize transaction:Deposit or withdraw")
        print("2.View all transactions")
      
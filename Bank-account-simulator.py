import logging
import random
from datetime import datetime
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_transaction_id():
    return f"TXN{random.randint(100000,999999)}"

class AccountNotFoundError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self,customer_name,customer_id,account_type,bal):
        self.customer_name=customer_name
        self.customer_id=customer_id
        self.account_type=account_type
        self.bal=bal
        
        
    def get_customer_info(self):
        return f"Customer Name:{self.customer_name},Account-type:{self.account_type},Balance:{self.bal}"
    
    
class BankAccountmngr:
        def __init__(self):
            self.accounts={}
            self.transaction_history={}
            
        def create_account(self,customer_name,customer_id,account_type,bal):
            if customer_id in self.accounts:
                logging.warning("Account with this customer ID already exists.")
                return
            account=Account(customer_name,customer_id,account_type,bal)
            self.accounts[customer_id]=account
            logging.info("Account created successfully.")
            
            
        def remove_account(self,customer_id):
            if customer_id in self.accounts:
                del self.accounts[customer_id]
                logging.info("Account deleted successfully.")
                
            else:
                logging.error("Account with this customer ID does not exist.")
                
        def get_account_info(self,customer_id):
            account=self.accounts.get(customer_id)
            if account:
                return account.get_customer_info()
            else:
                logging.error("Account with this customer ID does not exist.")
                return None
            
        def deposit(self,customer_id,amount):
            if customer_id not in self.accounts:
                raise AccountNotFoundError("Account with this customer ID does not exist.")
            if amount<=0:
                raise InvalidAmountError("Deposit amount must be positive.")
                
            self.accounts[customer_id].bal += amount
            txn_id=generate_transaction_id()
            self.transaction_history.setdefault(customer_id,[]).append({
                "transaction_id":txn_id,
                "type":"deposit",
                "amount":amount,
                "timestamp":datetime.now().isoformat()
            })
            logging.info(f"Deposited {amount}. New balance: {self.accounts[customer_id].bal}")
            
        def withdraw(self,customer_id,amount):
            if customer_id not in self.accounts:
                raise AccountNotFoundError("Account does not exist")
                
            if amount<=0:
                raise InvalidAmountError("Amount must be positive")
                
            if self.accounts[customer_id].bal<amount:
                raise InsufficientFundsError("Insufficient funds for withdrawal.")
                
            
            self.accounts[customer_id].bal -= amount
            
            txn_id=generate_transaction_id()
            self.transaction_history.setdefault(customer_id,[]).append({
                "transaction_id":txn_id,
                "type":"withdrawal",
                "amount":amount,
                "timestamp":datetime.now().isoformat()  
            })  
            
            logging.info(f"Withdrew {amount}. New balance: {self.accounts[customer_id].bal}")
                
        def get_transaction_history(self,customer_id):
            return self.transaction_history.get(customer_id,[])
            

if __name__=="__main__":
    account1=Account("Christine Mwende",32019034,"savings",3200)
    account2=Account("Chris Maembe",12012132,"business",120000)
    account3=Account("Paul Odera",23590819,"Business",320000)
    
    account_mngr=BankAccountmngr()
    account_mngr.create_account(account1.customer_name,account1.customer_id,account1.account_type,account1.bal)
    account_mngr.create_account(account2.customer_name,account2.customer_id,account2.account_type,account2.bal)
    account_mngr.create_account(account3.customer_name,account3.customer_id,account3.account_type,account3.bal)
    
    account_mngr.deposit(32019034,500)
    account_mngr.withdraw(12012132,2000)
    transaction_info=account_mngr.get_transaction_history(23590819)
                                
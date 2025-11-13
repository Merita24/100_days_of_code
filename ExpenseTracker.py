import os
import json

class Expenses:
  def __init__(self,name,cost_of_expense):
    self.name=name
    self.cost_of_expense=float(cost_of_expense)

  def to_dict(self):
    return {
       "name":self.name,
       "cost_of_expense":self.cost_of_expense 
            
    }
  


class ExpenseTracker:
  def __init__(self,income,filename='expensetracker.json'):
    self.income=income
    self.filename=filename
    self.expenses=self.load_expenses()
    

  def load_expenses(self):
    if not os.path.exists(self.filename):
      return []

    with open(self.filename,'r') as file:
      try:
        return json.load(file)

      except json.JsonDecodeError:
        return []

  def calculate_total_expenses(self):
      total=0.0
      for x in self.expenses:
        total=total + float(x['cost_of_expense'])
      return total

  def balance_after_expenses(self):
      tot=self.calculate_total_expenses()
      bal=self.income-tot
      return bal

  def calculate_savings(self):
    savings=0.05*self.income
    return savings

  def save_expense(self):
    with open(self.filename,'w') as file:
      json.dump(self.expenses,file,indent=4)

  def add_expense(self,expense):
    self.expenses.append(expense.to_dict())
    self.save_expense()

  def delete_expense(self):
    y=input("Enter the name of the expense you wish to delete:")
    found=False
    for x in self.expenses:
      if x['name']==y:
        self.expenses.remove(y)
        self.save_expenses()
        found=True
        print("Expense deleted successfully")
    if not found:
        print("Expense not found")
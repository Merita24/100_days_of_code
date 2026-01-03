import os
import json
from collections import defaultdict

class Expense:
    def __init__(self,name,price,priority):
        self.name=name
        self.price=price
        self.priority=priority
        
    def to_dict(self):
        return{
            "name":self.name,
            "price":self.price,
            "priority":self.priority
            
        }
    
class ExpenseCategorizer:
        def __init__(self,filename='expensecategorizer.json'):
            self.filename=filename
            self.expenses=self.load_expenses()
            
        def load_expenses(self):
            if not os.path.exists(self.filename):
                return []
            with open(self.filename,'r')as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        def save_expenses(self):
            with open(self.filename,'w') as file:
                json.dump(self.expenses,file,indent=4)
        def add_expense(self,expense):
            self.expenses.append(expense.to_dict())
            self.save_expenses()
        def search_expense(self,name):
            for x in self.expenses:
                if x['name'].lower()==name.lower():
                    return x
            return None
        def delete_expense(self,name):
           x=self.search_expense(name)
           if x:
               self.expenses.remove(x)
               self.save_expense()
               print("Expense deleted successfully")
           else:
               print("Expense does not exist")
        def categorize_expenses(self):
            categories=defaultdict(list)
            for x in self.expenses:
                if x['priority'].lower()=="high":
                    categories['High Priority'].append(x)
                elif x['priority'].lower()=="medium":
                    categories['Medium Priority'].append(x)
                elif x['priority'].lower()=="low":
                    categories['Low Priority'].append(x)
                else:
                    categories['Uncategorized'].append(x)
            return categories
        def sum_of_categories(self,priority):
            categories=self.categorize_expenses()
            for category, items in categories.items():
                if priority.lower()in category.lower():
                    return sum(map(lambda x:x['price'],items))
                
            return 0
                                
if __name__=="__main__" :
    while True :
        print("\n------Expense Categorizer")
        print("1.Add expense")  
        print("2.Search expense")
        print("3.Delete expense")
        print("4.Categorize expenses")
        print("5.Sum of items in a category")
        print("6.Exit")
        
        user=input("Enter your choice(1-6):")
        if user=="1":
            
            name=input("Enter expense name:")
            price=float(input("Enter expense price:"))
            priority=input("Enter expense priority(high/medium/low):")
            expense=Expense(name,price,priority)
            categorizer=ExpenseCategorizer()
            categorizer.add_expense(expense)
            print("Expense added successfully.")     
        elif user=="2":
            name=input("Enter expense name to search:")
            categorizer=ExpenseCategorizer()
            result=categorizer.search_expense(name)
            if result:
                print("Expense found:",result)          
            else:
                print("Expense not found.")
                
        elif user=="3":
            name=input("Enter expense name to delete:")
            categorizer=ExpenseCategorizer()
            categorizer.delete_expense(name)
        elif user=="4":
            categorizer=ExpenseCategorizer()
            categories=categorizer.categorize_expenses()
            for category,items in categories.items():
                print(f"\n{category}:")
                for item in items:
                    print(item)
        elif user=="5":
            cat=input("Enter category you want the sum for(high/medium/low):")
            if cat.lower()=="high" or cat.lower()=="medium" or cat.lower()=="low":
                categorizer=ExpenseCategorizer()
                total=categorizer.sum_of_categories(cat)
                print(f"Total sum of {cat} priority expenses:{total}")
            else:
                print("Invalid category choice.")
        elif user=="6":
            print("Exiting Expense Categorizer. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            
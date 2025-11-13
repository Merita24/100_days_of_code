from ExpenseTracker import ExpenseTracker,Expenses

def main():
  ex=ExpenseTracker(2500000)

  while True:
    print("\n-------EXPENSE TRACKER--------")
    print("1.Add an expense")
    print("2.Delete an expense")
    print("3.Calculate savings")
    print("4.Calculate total expenses")
    print("5.Calculate balance after expenses")
    print("6.Exit")

    choice=input("Enter your choice:")
    if choice=="1":
        name=input("name of expense:")
        cost=float(input("Cost of expense:"))
        expense=Expenses(name,cost)
        ex.add_expense(expense)

    elif choice=="2":
        ex.delete_expense()

    elif choice=="3":
        print(f"Savings:{ex.calculate_savings()}" )
    
    elif choice=="4":
        print(f"Total expenses:{ex.calculate_total_expenses()}")
        
    elif choice=="5":
        print(f"Balance after expenses is:{ex.balance_after_expenses()}")
        
    elif choice=="6":
        print("Goodbye")
        break
        
    else:
        print("Invalid choice,please try again")
        
if __name__=="__main__":
    main()
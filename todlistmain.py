from todolist import Todolist

def main():
    todo=Todolist()
    
    while True:
        print("\n----To-Do-List-Menu-----")
        print("1.Add an item")
        print("2.Delete an item")
        print("3.View all items")
        print("4.Exit")
        
        
        choice=input("Enter your choice:")
        if choice=="1":
            x=input("Enter the name of the item:")
            todo.add_item(x)
            
        elif choice=="2":
            todo.view_items()  
            try:
                index = int(input("Enter the item number to delete: ")) - 1
                todo.delete_item(index)  
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice=="3":
            todo.view_items()
        
        elif choice=="4":
            print("Goodbye!")
            break
        
if __name__=="__main__":
    main()
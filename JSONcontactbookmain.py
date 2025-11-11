from ContactBook import ContactBook,Contacts

def main():
  book=ContactBook()

  while True:
      
    print("\n----Contact Book-----")
    print("1. Add contact")
    print("2. View Contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
 

    choice=input("Please enter your choice:")


    if choice=="1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        contact=Contacts(name,phone,email)
        book.add_contact(contact)


    elif choice=="2":
      y=book.view_contact(contact)

    elif choice=="3":
      name=input("Enter the name to be searched:")
      x=book.search_contact(name)
      print(x if x else "contact not found")

    elif choice=="4":
        name=input("Enter name to be deleted:")
        z=book.delete_contact(name)
    elif choice=="5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
        
if __name__=="__main__":
    main()
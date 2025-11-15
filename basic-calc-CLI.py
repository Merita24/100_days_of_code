import logging

logging.basicConfig(
   filename='calculator.log',
   level=logging.INFO,
   format='%(asctime)s - %(levelname)s - %(message)s'
                    
)
def calculator():
    while True:
        
        print("\n -------BASIC CALCULATOR------")
        ex=input("Exit the calculator? type y/n:")
        if ex.lower()=="y":
            print("goodbye")
            break
    
        
        try:
            first_num=int(input("Enter the first number:"))
            sec_num=int(input("Enter the second number:"))
        except ValueError:
            print("Enter a valid number")
            logging.error("Invalid input from user")
            continue 
       
        print("Pick an operator")
        print("1.Addition(+)")
        print("2.Subtraction(-)")
        print("3.Multiplication(x)")
        print("4.Division(/)")
        print("5.Exit")
        choice=input("Enter your choice:")


        if choice=="1":
            print(f"The addition of {first_num} and {sec_num} is {first_num+sec_num}")
            logging.info(f"Added {first_num} and {sec_num}")

        elif choice=="2":
            print(f"The subtraction of {first_num} and {sec_num} is {first_num-sec_num}")
            logging.info(f"Subtracted {sec_num} from {first_num}")

        elif choice=="3":
            
            print(f"The multiplication of {first_num} and {sec_num} is {first_num*sec_num}")
            logging.info(f"Multiplied {first_num} and {sec_num}")

        elif choice=="4":
            if sec_num==0:
                print("Cannot divide number by zero")
                logging.error("division by zero attempted")
                
            else:    
                print(f"The dvision of {first_num} and {sec_num} is {first_num/sec_num}")
                logging.info(f"Divided {first_num} by {sec_num}")

        elif choice=="5":
            print("Goodbye")
            logging.info("You exited the calculator")
            break


        else:
            print("Invalid input")
            logging.warning("You attempted an invalid operation")

if __name__=="__main__":
    calculator()
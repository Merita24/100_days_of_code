
import itertools
while True:
    print("Welcome to the Multiplication Table Generator! ")
    while True:
        try:
            N=int(input("Enter a number N to generate an N x N multiplication table: "))
            if N<=0:
                print("Please enter a positive integer greater than zero.")
                continue
            break
        except ValueError:
         print("Invalid input. Please enter a valid integer.")
        continue
    
    for i,j in itertools.product(range(1,N+1),repeat=2):
        print(f"{i} x {j}={i*j}")

    cont=input("Do you want to generate another table? (y/n): ")
    if cont.lower() !='y':
      print("Thank you for using the Multiplication Table Generator. Goodbye!")
      break
   
class Customer:
    def __init__(self,name,customer_id,email,phone_number,location,):
        self.name=name
        self.customer_id=customer_id
        self.email=email
        self.phone_number=phone_number
        self.location=location
        
    def __str__(self):
        return f"{self.name} ({self.customer_id})"

        
    
class Product:
    def __init__(self,product_id,price,quantity,brand,category,description):
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.product_id=product_id
        self.price=price
        self.quantity=quantity
        self.brand=brand
        self.category=category
        self.description=description
        
    def __str__(self):
        return f"{self.product_id} | {self.brand} | ${self.price} | Stock: {self.quantity}"

            
class ShoppingCart:
    def __init__(self,customer_id):
           self.customer_id=customer_id
           self.cart={}
           self.shopping_history={}
           
    def add_to_cart(self,product,quantity):
       if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
       if quantity > product.quantity:
            raise ValueError("Not enough stock available")

       self.cart[product.product_id] = self.cart.get(product.product_id, 0) + quantity
       product.quantity -= quantity
            
        
    def remove_from_cart(self,product,quantity):
        if product.product_id not in self.cart:
            raise ValueError("Product not in cart")
        if quantity > self.cart[product.product_id]:
            raise ValueError("Cannot remove more than in cart")

        self.cart[product.product_id] -= quantity
        product.quantity += quantity

        if self.cart[product.product_id] == 0:
            del self.cart[product.product_id]
            
      
           
    def checkout(self, products):
        if not self.cart:
              raise ValueError("Cart is empty")
        total = 0
        receipt = []

        for product_id, quantity in self.cart.items():
            product = products[product_id]
            cost = product.price * quantity
            total += cost
            receipt.append({
                "product_id": product_id,
                "quantity": quantity,
                "total_price": cost
            })

        self.shopping_history.extend(receipt)
        self.cart.clear()

        return total
class EcommerceSystem:
    def __init__(self):
        self.customers={}
        self.products={}
        self.shopping_carts=()
        
    def add_customer(self, customer):
        if customer.customer_id in self.customers:
            raise ValueError("Customer already exists")

        self.customers[customer.customer_id] = customer
        self.shopping_carts[customer.customer_id] = ShoppingCart(customer.customer_id)
        
    def add_product(self, product):
        if product.product_id in self.products:
            raise ValueError("Product already exists")

        self.products[product.product_id] = product

    def display_products(self):
        if not self.products:
            print("No products available.")
            return
        for product in self.products.values():
            print(product)
        
        
if __name__=="__main__":
    ecom=EcommerceSystem()
    
    while True:
        print("\n--- LALA E-COMMERCE SYSTEM ---")
        print("1. Add Customer")
        print("2. Add Product")
        print("3. View Products")
        print("4. Add to Cart")
        print("5. Checkout")
        print("6. View Shopping History")
        print("7. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                customer_id = input("Customer ID: ")
                name = input("Name: ")
                email = input("Email: ")
                phone = input("Phone: ")
                location = input("Location: ")

                customer = Customer(name, customer_id, email, phone, location)
                ecom.add_customer(customer)
                print("Customer added successfully.")

            elif choice == "2":
                product_id = input("Product ID: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                brand = input("Brand: ")
                category = input("Category: ")
                description = input("Description: ")

                product = Product(product_id, price, quantity, brand, category, description)
                ecom.add_product(product)
                print("Product added successfully.")

            elif choice == "3":
                ecom.display_products()

            elif choice == "4":
                customer_id = input("Customer ID: ")
                product_id = input("Product ID: ")
                quantity = int(input("Quantity: "))

                cart = ecom.shopping_carts[customer_id]
                product = ecom.products[product_id]

                cart.add_to_cart(product, quantity)
                print("Product added to cart.")

            elif choice == "5":
                customer_id = input("Customer ID: ")
                cart = ecom.shopping_carts[customer_id]

                total = cart.checkout(ecom.products)
                print(f"Checkout successful. Total amount: ${total}")

            elif choice == "6":
                customer_id = input("Customer ID: ")
                history = ecom.shopping_carts[customer_id].shopping_history

                if not history:
                    print("No shopping history.")
                else:
                    for item in history:
                        print(item)

            elif choice == "7":
                print("Goodbye 👋")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print(f"Error: {e}")
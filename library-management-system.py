import re
EMAIL_REGEX=re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def validate_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email))

def normalize_phone(phone: str) -> str:
    return "".join(char for char in phone if char.isdigit())

def validate_phone(phone: str) -> bool:
    digits = normalize_phone(phone)
    return 10 <= len(digits) <= 15


class MemberNotFoundError(Exception):
    pass
class MemberAlreadyExistsError(Exception):
    pass
class BookNotAvailableError(Exception):
    pass

class StockAvailabilityError(Exception):
    pass

class InvalidPhoneNumberError(Exception):
    pass

class InvalidEmailError(Exception):
    pass
class BookNotInCartError(Exception):
    pass





class Book:
    def __init__(self,title,book_id,author,isbn,copies):
        self.title=title
        self.book_id=book_id
        self.author=author
        self.isbn=isbn
        self.copies=copies
        
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
        
        
class Member:
    def __init__(self,name,member_id,email,phone_number):
        if not validate_email(email):
             raise InvalidEmailError("Invalid email format.")
        if not validate_phone(phone_number):
            raise InvalidPhoneNumberError("Invalid phone number format.")            
        self.name=name
        self.member_id=member_id    
        self.email=email
        self.phone_number=phone_number
            
    def __str__(self):
        return f"{self.name} ({self.member_id})"
        
class BookCart:
    def __init__(self,member_id):
            self.member_id=member_id
            self.cart={}
            self.borrowing_history=[]
            
    def add_to_cart(self,book,copies):
            if copies<=0:
                 raise ValueError("Book copies must be greater than zero")
            if copies>book.copies:
                raise StockAvailabilityError("Not enough copies available")
            
            self.cart[book.book_id]=self.cart.get(book.book_id,0)+copies
            book.copies-=copies
                
    def remove_from_cart(self,book,copies):
            if book.book_id not in self.cart:
                raise BookNotInCartError("Book not in cart")
            if copies>self.cart[book.book_id]:
                raise ValueError("Cannot remove more than in cart")
            self.cart[book.book_id]-=copies
            if self.cart[book.book_id] == 0:
                del self.cart[book.book_id]
            book.copies+=copies
            
            
    def checkout(self,books):
            if not self.cart:
                raise ValueError("Cart is empty")
            books_borrowed=[]
            for book_id,copies in self.cart.items():
                book=books.get(book_id)
                copies_taken=self.cart[book_id]
                if book:
                    books_borrowed.append({
                        "book_id":book.book_id,
                        "title":book.title,
                        "author":book.author,
                        "copies":copies_taken
                    })
                
            self.borrowing_history.extend(books_borrowed)
            self.cart.clear()
            
                
                
                
                
                
class LibraryManager:
    def __init__(self):
        self.members={}
        self.books={}
        self.carts={}
        
        
    def register_member(self,member):
        if member.member_id in self.members:
            raise MemberAlreadyExistsError("Member ID already exists")
        self.members[member.member_id]=member
        self.carts[member.member_id]=BookCart(member.member_id)
        
    def add_book(self,book):
        if book.book_id in self.books:
            raise ValueError("Book ID already exists")
        self.books[book.book_id]=book
    
    def display_available_books(self):
        if not self.books:
            raise BookNotAvailableError("No books available in the library")
        available_books=[book for book in self.books.values() if book.copies>0]
        return available_books
            
            
    
if __name__=="__main__":
    lib=LibraryManager()
        
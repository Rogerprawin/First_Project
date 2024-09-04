# question 1
'''Create a Class: Define a Car class with attributes like make, model, and year. 
Include a method display_info that prints out the car's information in a 
readable format.'''

'''class car:
    
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def display_info(self):
        print("make:",self.make)
        print("model",self.model)
        print("year",self.year)

honda=car("civic","japan",2018)
honda.display_info()'''

#question 2
'''Implement a Constructor: Create a Book class with attributes title, author, 
and year_published.Implement the __init__ method to initialize these attributes 
when creating a new book object.'''

'''class book:

    def __init__(self,title,author,published):
        self.title=title
        self.author=author
        self.published=published

    def display(self):
        print("title of the book:",self.title)
        print("author of thr book:",self.author)
        print("year the book was published:",self.published)

Book=book("GUNS AND ROSES","LISA",2001)
Book.display()'''

#question 3:
'''Inheritance: Define a base class Animal with attributes name and age, and a method make_sound. 
Create a subclass Dog that inherits from Animal and overrides the make_sound method 
to return a specific sound like "Woof".'''

'''class animal:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def make_sound(self):
        pass

class Dog(animal):
    def __init__(self,name,age):
      self.name=name
      self.age=age

    def sound(self):
        print ("woof")
    
dog=Dog("jimmy",5)
dog.sound()'''

#question 4

'''Class vs. Instance Variables: Create a BankAccount class with an instance variable balance and
 a class variable interest_rate. Implement methods to deposit, withdraw, and 
 calculate the interest based on the class variable.'''

'''class BankAccount:
    interest_rate = 0.03 

    def __init__(self, balance):
        self.balance = balance
        balance=0
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def calculate_interest(self):
        interest = self.balance * BankAccount.interest_rate
        return interest

    def apply_interest(self):
        interest = self.calculate_interest()
        self.balance += interest
        print(f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}")

account = BankAccount(1000.00)  # Create an account with an initial balance of $1000
account.deposit(500.00)         # Deposit $500
account.withdraw(200.00)        # Withdraw $200
account.apply_interest()        # Apply interest based on the class variable'''

#question 5

''' Method Overriding: Create a base class Shape with a method area.
 Derive classes Rectangle and Circle from Shape and override the area method 
 to calculate the area for each shape.'''
'''import math
class shape:
    def area(self):
        pass

class rectangle(shape):

    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    
class circle(shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi * (self.radius **2)

rec=rectangle(3,4)
circ=circle(5)

print("Area of the rectangle:", rec.area())
print("Area of the circle: ",circ.area())    '''

#question 6

'''Encapsulation: Define a class Person with private attributes _name and _age. 
Provide public methods set_name, get_name, set_age, and get_age to access  and modify these attributes.'''

'''class person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def set_name(self,name):
        if isinstance(name, str) and name:
            self._name = name
        else:
            print("Invalid name")
        
    def get_name(self):
        return self._name

    def set_age(self,age):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            print("Invalid age")
    
    def get_age(self):
        return self._age
    
per=person("roger",25)

print("Name:",per.get_name())
print("Age:",per.get_age())

# Updating attributes
per.set_name("Roger prawin")
per.set_age(26)

print("Updated Name:",per.get_name())
print("Updated Age:",per.get_age())'''

#question 7

'''Define a Person class with a class method from_birth_year that creates a Person object using the 
birth year and current year.Include an __init__ method to initialize the person's name and age.'''

'''from datetime import datetime

class person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age)

    def display_info(self):
        print("Name:" , self.name)
        print("Age:" , self.age)

person = person.from_birth_year("Roger", 2000)
person.display_info()'''

#question 8 (done with the assitance of chatgpt)
'''Composition: Create a Library class that contains a collection of Book objects.
 Implement methods to add a book, remove a book, and list all books in the library.'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"'{self.title}' by {self.author}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Only Book objects can be added to the library.")
        self.books.append(book)
        print("Added:" , book)

    def remove_book(self, title):
        for book in self.books[:]:
            if book.title == title:
                self.books.remove(book)
                print("Removed:", book)
                return
        print(f"No book found with title: '{title}'")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
            return
        print("Books in the library:")
        for book in self.books:
            print(book)
if __name__ == "__main__":
    library = Library()
    
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    
    library.add_book(book1)
    library.add_book(book2)
    library.list_books()
    library.remove_book("1984")
    library.list_books()


        

class Student:

    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

student1=Student("John", "Doe", 20)
student2=Student("Salim", "Smith", 22)

print(student1.first_name) 
print(student2.second_name) 
# 1.


class Car:
    
    def __init__ (self, model,year,color,speed):
        self.model=model
        self.year=year
        self.color=color
        self.speed=speed
        
car1=Car("Toyota", 2020, "Red", 120)
car2=Car("Honda", 2019, "Blue", 110)

print(car1.model,car1.year,car1.color,car1.speed)
print(car2.model,car2.year,car2.color,car2.speed)
# 3.
class Person:
    
    def __init__ (self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def greet(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am {self.gender}.")

person1 = Person("Manas",20,"Male")

person1.greet()    

# 5.

class Rectangle:
    
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def area(self):
        print(self.length * self.width)
    def perimeter(self):
        print(  2*(self.length+self.width))
    
rectangle1=Rectangle(5,3)

rectangle1.area()
rectangle1.perimeter()

# 8.
class BankAccount:
    
    def __init__ (self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposit successful. New balance is {self.balance}")
    def withdraw(self,amount):
        self.balance-=amount
        print(f"withdraw successful. New balance is {self.balance}")
        
account1=BankAccount("Manas",20000)
account1.deposit(5000)
account1.withdraw(3000)

# 11.

class Dog:
    
    def __init__ (self,breed,age):
        self.breed=breed
        self.age=age
        
    def bark(self):
        print("Woof!")
        
dog1=Dog("Labrador",3)
dog1.bark()

# 13.

class Book:
    
    def __init__ (self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def short_description(self):
        print(f"{self.title} is a book written by {self.author}")

book1=Book("To Kill a Mockingbird","Harper Lee",281)

book1.short_description() 
# 15.
class Laptop:
    
    def __init__ (self,brand,ram_size):
        self.brand=brand
        self.ram_size=ram_size
    def upgrade_ram(self,size):
        self.ram_size+=size
        print(f"RAM upgraded succesfully. New RAM size is {self.ram_size}")

laptop1=Laptop("ASUS",8)

laptop1.upgrade_ram(8)

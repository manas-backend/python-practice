 # 1. Car nomli class yaratamiz
class Car:
    wheels = 4   # 2. Class atribut

    def __init__(self, model, color):
        self.model = model      # instance atribut
        self.color = color      # instance atribut

    # 3. __str__ metodi
    def __str__(self):
        return f"Model: {self.model}, Color: {self.color}"


# Obyektlar yaratamiz
car1 = Car("BMW", "Black")
car2 = Car("Tesla", "White")

# 1. Instance atributlarni chiqarish
print(car1.model)
print(car1.color)

# 2. Class atributni chiqarish
print(car1.wheels)
print(car2.wheels)

# 3. Obyektni to‘g‘ridan-to‘g‘ri chop etish
print(car1)
print(car2)

# 2.
class Book:
    
    bet=201
    def __init__(self,title,author):
        self.title=title
        self.author=author
        
    def __repr__(self):
        return f"book title: {self.title}, book author: {self.author}"
    def __len__(self):
        return self.bet
    
    
book1= Book("Kuzda gullamoqchi bolgan men", "Manas")

print(book1.title)
print(book1.author)
print(book1.bet)
print(book1)

print(len(book1))
# 3.

class Student:
    school_name="TUIT"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @classmethod
    def change_school(cls,new_school):
        cls.school_name=new_school
        
student1=Student("Ali",20)
student=Student("Vali",22)

print(student1.school_name)

Student.change_school("TUIT University")

print(student1.school_name)

# 4.

class MathTools:
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def ayiruv(a,b):
        return a-b
        
q1=MathTools.add(5,4)
q2=MathTools.ayiruv(10,4)

print(q1)
print(q2)

# 5.
class Employee:
    
    company_name="Najot talim"
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    @classmethod
    def change_company(cls,new_company):
        cls.company_name = new_company
        
    def work_info(self):
        return f"{self.name},va salary {self.salary}"
    
    def __str__(self):
        return f"{self.name} salary: {self.salary}, Company name: {self.company_name}"
q1=Employee("Salim",1000)
w1=Employee("Asqar",1200)

print(q1)
print(w1)

print(q1.work_info())

Employee.change_company("NEW COMPANY")

print(q1)
print(w1)

# 6.

class Rectangle():
    
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def __str__(self):
        return f"width: {self.width}, height: {self.height}"
        
    @staticmethod
    def is_valid(value):
        return "Valid" if value>0 else "Invalid"
            
q1=Rectangle(5,6)
w1=Rectangle(3,4)

print(q1)
print(w1)

print(Rectangle.is_valid(8))
print(Rectangle.is_valid(-8))

# 7.

class Product:
    
    def __init__(self,name,price):
        self.name = name
        self.price = price 
    
    def __str__(self):
        return f"{self.name}  (${self.price})"
        
    def __eq__(self,a):
        return self.price==a.price
        
q1=Product("Apple",50)
w1=Product("Limon",50)

print(q1)
print(w1)

print(q1==w1)




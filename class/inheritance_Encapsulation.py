# 1.

class Person:
    
    def __init__(self, name, age):
        self.name=name
        self.__age=age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age>21:
            self.__age=age
        else:
            print("Invalid age!")
    
    def __str__(self):
        return f"Person: {self.name}"   
    
q1=Person("Salim", 25)

print(q1)
print(q1.get_age())

q1.set_age(3)
print(q1.get_age())

# 2.

class Account:
    
    def __init__(self, balance):
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance +=amount
        
    def withdraw(self,amount):
        a=int(input("Enter amount of money to withdraw: "))
        if self.__balance>=a:
            self.__balance-=a
        else:
            print("Not enough balance!!!")
            
w1=Account(10000)

print(w1.get_balance())

w1.deposit(5000)
print(w1.get_balance())

w1.withdraw(3000)
print("Your balance is: ",w1.get_balance())

# 3.

class Car:
    
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed
        
    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed<=50:
            self.__speed = speed
        else:
            print("Your is too fast!!!")
            
    def private_password(self):
        return "This is a private method!!!"
    
    
q1=Car("BMW", 50)
print(q1.brand)
print(q1.get_speed())

q1.set_speed(60)
print(q1.get_speed())

# 4.

class Animal:
    
    def __init__(self, name, sound):
        
        self.name = name
        self.sound = sound
        
class Dog(Animal):
    
    def __init__(self, name, sound):
        super().__init__(name, sound)

class Cat(Animal):
    
    def __init__(self, name, sound):
        super().__init__(name, sound)
    
q1=Dog("Rex", "Woof")
q2=Cat("Scar", "Meow")

print(q1.name)
print(q1.sound) 

print(q2.name)
print(q2.sound) 

# 5.

class Shape:
    
    def __init__(self):
        pass
        
class Reactangle(Shape):
    
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        
    def area(self):
        return(self.width*self.height)
    
class Circle(Shape):
    
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        
    def area(self):
        return(3.14*self.radius**2)

q1=Reactangle(5,6)
w1=Circle(3)

print(q1.area())
print(w1.area())
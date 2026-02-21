#  # 1. Car nomli class yaratamiz
# class Car:
#     wheels = 4   # 2. Class atribut

#     def __init__(self, model, color):
#         self.model = model      # instance atribut
#         self.color = color      # instance atribut

#     # 3. __str__ metodi
#     def __str__(self):
#         return f"Model: {self.model}, Color: {self.color}"


# # Obyektlar yaratamiz
# car1 = Car("BMW", "Black")
# car2 = Car("Tesla", "White")

# # 1. Instance atributlarni chiqarish
# print(car1.model)
# print(car1.color)

# # 2. Class atributni chiqarish
# print(car1.wheels)
# print(car2.wheels)

# # 3. Obyektni to‘g‘ridan-to‘g‘ri chop etish
# print(car1)
# print(car2)

# # 2.
# class Book:
    
#     bet=201
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
        
#     def __repr__(self):
#         return f"book title: {self.title}, book author: {self.author}"
    
# book1= Book("Kuzda gullamoqchi bolgan men", "Manas")

# print(book1.title)
# print(book1.author)
# print(book1.bet)
# print(book1)

# 3.

class Student:
    
    school_name= "Oxford"
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
s1=Student("Ali", 20)   
s2=Student("Vali", 22)

print(s1.school_name)
print(s2.school_name)
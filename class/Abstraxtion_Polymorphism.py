from abc import ABC, abstractmethod

class Transport(ABC):
    
    total_vehicles = 0
    
    def __init__(self, brand, speed, id):
        self.brand = brand
        self.speed = speed
        self.__id = id
        Transport.total_vehicles += 1
        
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    def get_id(self):
        return self.__id
    
    @staticmethod
    def is_valid_speed(speed):
        if speed>=0:
            return speed
        else:
            return "Invalid speed!!!"

class Car(Transport):
    
    def __init__(self,brand,speed, id, fuel):
        super().__init__(brand, speed, id)
        self.fuel= fuel 
        
    def start(self):
        print(f"{self.brand} started. Fuel level: {self.fuel}")
    
    def move(self):
        print(f"{self.brand} is moving. speed: {self.speed}")
    
    def stop(self):
        print(f"{self.brand} has stopped.")
        
class Bus(Transport):
    
    def __init__(self,brand, speed, id, capacity):
        super().__init__(brand, speed, id)
        self.capacity = capacity
        
    def start(self):                
        print(f"{self.brand} started. Capacity: {self.capacity}")
    
    def move(self):
        print(f"{self.brand} is moving. speed: {self.speed}")
    
    def stop(self):
        print(f"{self.brand} has stopped.")
        
class Bicycle(Transport):
    
    def __init__(self, brand, speed, id, type):
        super().__init__(brand, speed, id)
        self.type = type
        
    def gear_count(self):
        return 10 if self.type=="mountain" else 5
    
    def start(self):
        print(f"{self.brand} started: Type: {self.type}")
        
    def move(self):
        print(f"{self.brand} is moving. speed: {self.speed}")
    
    def stop(self):
        print(f"{self.brand} has stopped.")

class Scooter(Transport):
    
    def __init__(self,brand,speed,id,power):
        super().__init__(brand,speed,id)
        self.power=power
        
    def battery(self):
        print(f"Power {self.power}%")

    def start(self):
        print(f"{self.brand} is moving, Power: {self.power}%")
    
    def move(self):
        print(f"{self.brand} is moving. speed: {self.speed}")
    
    def stop(self):
        print(f"{self.brand} has stopped.")  
        
c1 = Car("BMW", 120, "123ads", 50)
b1 = Bus("№63", 80, "456def", 50)
d1 = Bicycle("Trek", 20, "789ghi", "mountain")
w1 = Scooter("Xiaomi", 25, "321jkl", 80)

print(c1.get_id())
print(b1.get_id())
print(d1.get_id())
print(w1.get_id())

all_transports = [c1, b1, d1, w1]

for vehicle in all_transports:
    vehicle.start()
    vehicle.move()
    vehicle.stop()

for i in all_transports:
    i.get_id()
    
    
print(Transport.total_vehicles)

print(Transport.is_valid_speed(120))
print(Transport.is_valid_speed(-10))
    

print(c1.brand)
print(c1.speed)
print(c1.fuel)

print("----")
print(b1.brand)
print(b1.speed)
print(b1.capacity)


print("----")
print(d1.brand)
print(d1.speed)
print(d1.type)


print("----")
print(w1.brand)
print(w1.speed)
print(w1.power)

print("----")

print(d1.gear_count())
print(w1.battery())
print("----")
print(w1.get_id())

from abc import ABC, abstractmethod

class Transport(ABC):
    total_vehicles = 0  # class atribut

    def __init__(self, brand, speed, id):
        self.brand = brand
        self.speed = speed
        self.__id = id      # private atribut
        Transport.total_vehicles += 1  # har yangi obyektda +1

    # Abstract metodlar
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    # Protected metod
    def _get_info(self):
        return f"Brand: {self.brand}, Speed: {self.speed}, ID: {self.get_id()}"

    def get_id(self):
        return self.__id

    # Static metod
    @staticmethod
    def is_valid_speed(speed):
        return speed >= 0

class Car(Transport):
    def __init__(self, brand, speed, id, fuel):
        super().__init__(brand, speed, id)  # Transport klassining __init__ chaqirildi
        self.fuel = fuel                    # yangi atribut

    # Abstract metodlarni amalga oshirish
    def start(self):
        print(f"{self.brand} started. Fuel level: {self.fuel}L")

    def move(self):
        if self.is_valid_speed(self.speed):
            print(f"{self.brand} is moving at {self.speed} km/h")
        else:
            print("Invalid speed!")

    def stop(self):
        print(f"{self.brand} has stopped.")
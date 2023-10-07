# prevents a user from creating an object of the class
# and compels a user to override absract methods in a child class

# abstract class =      a class which contains one or more abstract methods
# abstract method =     a method that has a declaration but is not implemented

from abc import ABC, abstractmethod         # abs module contains base abstract class, from which our Vehicle class will inehrit the properties that makes it abstract.
                                            # abstractmethod is a decorator used to modify methods so they become abstract methods,
                                            # also needs to be imported from abc module

class Vehicle(ABC):
    
    @abstractmethod     # decorator that makes the method abstract
    def go(self):
        pass

class Car(Vehicle):
    def go(self):       # this method needs to be implemented before creating a car object
        print("You drive the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")        # this method needs to be implemented before creating a motorcycle object

#vehicle = Vehicle()            # TypeError. can't create an object of an abstract class          
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()
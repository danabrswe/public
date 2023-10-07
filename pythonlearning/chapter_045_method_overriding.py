# note: "eat(self)" is the method signature of the eat method. signatures consist of the name + parameters.

class Animal:

    def eat(self):
        print("This animal eats")

class Rabbit(Animal):
    
    def eat(self):              # more spefici implementation of eat for the Rabbit class. this method overrides eat() in Animal class.
        print("This rabbit eats a carrot")

rabbit = Rabbit()
rabbit.eat()
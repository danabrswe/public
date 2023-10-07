# multiple inheritance =        when a child class is derived from more than one parent class

class Prey:

    def flee(self):
        print("This animal flees")

class Predator:

    def hunt(self):
        print("This animal hunts")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
#rabbit.hunt()      # attribute error: has no "hunt" attribute
hawk.hunt()
print("---")
fish.flee()
fish.hunt()
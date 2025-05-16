# Superhero class with encapsulation
class Superhero:
    def __init__(self, name, power, real_identity):
        self.name = name                # public attribute
        self.power = power              # public attribute
        self.__real_identity = real_identity  # private attribute

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

    def reveal_identity(self):
        return f"{self.name}'s real identity is {self.__real_identity}"

# Inherited class with additional ability
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, real_identity, flight_speed):
        super().__init__(name, power, real_identity)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")

# Create instances
hero1 = Superhero("ShadowStrike", "Invisibility", "Liam Gray")
hero2 = FlyingSuperhero("SkyFlash", "Electric Shock", "Aria Nova", 300)

# Interact with them
hero1.use_power()
print(hero1.reveal_identity())

hero2.use_power()
hero2.fly()
print(hero2.reveal_identity())

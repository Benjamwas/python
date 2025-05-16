class Superhero:
    def __init__(self, name, power, real_identity):
        self.name = name
        self.power = power
        self.__real_identity = real_identity  # Encapsulated attribute (private)

    def use_power(self):
        print(f"{self.name} uses their power: {self.power}!")

    def reveal_identity(self):
        return f"{self.name}'s secret identity is {self.__real_identity}."


class FlyingSuperhero(Superhero):
    def __init__(self, name, power, real_identity, flight_speed):
        super().__init__(name, power, real_identity)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")

    # Overriding use_power for a special flying power message (polymorphism)
    def use_power(self):
        print(f"{self.name} soars through the sky with {self.power}!")


# Testing
hero1 = Superhero("Shadow", "Invisibility", "Liam Gray")
hero2 = FlyingSuperhero("Skybolt", "Lightning", "Aria Nova", 320)

hero1.use_power()
print(hero1.reveal_identity())

hero2.use_power()
hero2.fly()
print(hero2.reveal_identity())

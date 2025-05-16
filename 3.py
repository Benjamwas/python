class Vehicle:
    def move(self):
        pass  # Base method to be overridden


class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road.")


class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky.")


class Boat(Vehicle):
    def move(self):
        print("🚢 Sailing on the water.")


# Polymorphic function
def make_vehicle_move(vehicle):
    vehicle.move()


# Instances
car = Car()
plane = Plane()
boat = Boat()

vehicles = [car, plane, boat]

for v in vehicles:
    make_vehicle_move(v)
class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_life_hours):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.__battery_life_hours = battery_life_hours  # Encapsulated (private)

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def check_battery(self):
        print(f"Battery life remaining: {self.__battery_life_hours} hours")

    def charge(self, hours):
        self.__battery_life_hours += hours
        print(f"Charged for {hours} hours. Battery life now {self.__battery_life_hours} hours.")


# Inheritance example: A Smartphone with camera capabilities
class CameraSmartphone(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_life_hours, camera_megapixels):
        super().__init__(brand, model, storage_gb, battery_life_hours)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels}MP camera on {self.brand} {self.model}!")


# Testing
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 24)
phone2 = CameraSmartphone("Apple", "iPhone 14", 256, 20, 12)

phone1.make_call("123-456-7890")
phone1.check_battery()
phone1.charge(2)

phone2.make_call("098-765-4321")
phone2.take_photo()
phone2.check_battery()

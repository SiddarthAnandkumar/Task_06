class Vehicle:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def rent_amount(self, days):
        return self.rate * days

class Car(Vehicle):
    def __init__(self, name, rate, seats):
        super().__init__(name, rate)
        self.seats = seats

    def rent_amount(self, days):
        extra = 200
        total = (self.rate + extra) * days
        return total

class Bike(Vehicle):
    def __init__(self, name, rate, helmet):
        super().__init__(name, rate)
        self.helmet = helmet

    def rent_amount(self, days):
        disc = 0
        if not self.helmet:
            disc = 50
        total = (self.rate - disc) * days
        return total

class Truck(Vehicle):
    def __init__(self, name, rate, load):
        super().__init__(name, rate)
        self.load = load

    def rent_amount(self, days):
        extra = 0
        if self.load > 1000:
            extra = 500
        total = (self.rate + extra) * days
        return total


if __name__ == "__main__":
    car1 = Car("Tata Punch", 2500, 6)
    bike1 = Bike("Jawa 42", 700, True)
    truck1 = Truck("Tata Tipper", 5000, 2500)

    print("---- Car Details ----")
    print("Name:", car1.name)
    print("Rent for 3 days: ₹", car1.rent_amount(7))

    print("\n---- Bike Details ----")
    print("Name:", bike1.name)
    print("Rent for 5 days: ₹", bike1.rent_amount(15))

    print("\n---- Truck Details ----")
    print("Name:", truck1.name)
    print("Rent for 2 days: ₹", truck1.rent_amount(20))

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return 'марка машины:' + self.model + 'модель машины:' + self.make
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
            return 'Марка машины: ' + self.make + ', модель машины: ' + self.model + ', тип топлива: ' + self.fuel_type
car = Car('Toyota','AGDY45','diesel')
print(car.get_info())
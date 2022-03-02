class Device:
    def __init__(self, type, model, data):
        self.type = str(type)
        self.model = str(model)
        self.date = str(data)
class CoffeMachine(Device):
    def __init__(self, type, model, date, price, year, typeOfCoffe):
        super(CoffeMachine, self).__init__(type, model, date)
        self.price = int(price)
        self.year = int(year)
        self.type_of_coffe = str(typeOfCoffe)
class Blender(Device):
    def __init__(self, type, model, date, power, size):
        super(Blender, self).__init__(type, model, date)
        self.power = int(power)
        self.size = float(size)
class MeatGrinder(Device):
    def __init__(self, type, model, date, typeOfMeat, energy):
        super(MeatGrinder, self).__init__(type, model, date)
        self.typeOfMeat = str(typeOfMeat)
        self.energy = int(energy)

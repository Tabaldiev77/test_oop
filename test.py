class Cars:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year


    def get_cars(self):
        return f'\nbrand = {self.brand}\nmodel = {self.model}\ncolor = {self.color}\nyear = {self.year}'


class SuperCars(Cars):
    def __init__(self, brand, model, color, year, speed, turbina, obm):
        super(SuperCars, self).__init__(brand, model, color, year)
        self.speed = speed
        self.turbina = turbina
        self.obm = obm


    def get_cars(self):
        return super(SuperCars, self).get_cars() + f'\nspeed = {self.speed}\nturbina = {self.turbina}\nobm = {self.obm}'


test = SuperCars('BMW', 'M8', 'black', '2024', '700', True, '8.8')
print(test.get_cars())



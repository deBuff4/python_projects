class circle:
    def  __init__(self, radius = 20):
        self.radius = radius
    def get_radius(self):
        return 'Изначальный радиус ' + str(self.radius)
    def set_radius(self, new_r):
        self.radius =   new_r()
Circle =circle(2)
Circle.get_radius()
print(Circle.get_radius())
# print(Circle.set_radius())
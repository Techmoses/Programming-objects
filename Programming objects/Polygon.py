class Polygon:
    width = 0
    height = 0
    def set_values(self, width, height):
        Polygon.width = width
        Polygon.height = height
        
from Polygon import *
class Rectangle(Polygon):
    def area(self):
        return (self.width*self.height)
    
from Polygon import *
class Triangle(Polygon):
    def area(self):
        return (self.width*self.height)/2
from Rectangle import *
from Triangle import *

rect = Rectangle()
trey = Triangle()

rect.set_values(4,5)
trey.set_values(4,5)

print('Rectangle Area:', rect.area())
print('Triangle Area:', trey.area())

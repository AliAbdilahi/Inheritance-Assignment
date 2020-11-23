class Circle():
    def __init__(self, radius, color):
        self.__radius = float(radius)
        self.__color = color
    def getradius(self):
        return (self.__radius)
    def setradius(self):
        self.__radius = input("set radius to?")
        return (self.__radius)
    def getColor(self):
        return (self.__color)
    def setColor(self):
        self.__color= "set color to?"
        return (self.__color)
    def getArea(self):
        return ((self.__radius**2)*3.14)
    def toString(self):
        return (str(self.__radius)+" is "+ self.__color)
circle = Circle(1.5, "red")
class Cylinder(Circle):
    def __init__(self, radius, color, height):
        super().__init__(radius, color)
        self.__height = float(height)
    def getHeight(self):
        return (self.__height)
    def setradius(self):
        self.__height = input("set height to?")
        return (self.__height)
    def getVolume(self):
        return(super().getArea()* self.__height)
    def toString(self):
        return ("Cylinder is "+ super().getColor()+" with height "+str (self.__height))
cylinder= Cylinder(1.5, "red", 1.0)
    
print(cylinder.toString())

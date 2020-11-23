class Person():
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
    def getname(self):
        return (self.__name)
    def getaddress(self):
        return(self.__address)
    def setaddress(self):
        self.__address= "Unknown!"
        return(self.address)
    def tostring(self):
        return (self.__name+"("+self.__address+")")
class student(Person):
    def __init(self, name, address, numcourses):
        super().__init__(name, address)
        self.__numcourses= numcourses
        self.__courses= []
        self.__grades = []
    def addcoursesgrade(courses, grades):
        self.__courses += courses
        self.__grades += float(grades)
    def printgrades(self):
        return (self.__grades)
    def getaveragegrade(self):
        return (sum(grades)/len(grades))
    def tostring(self):
        return( super().getaddress())
class Teacher(Person):
    def __init(self, name, address, numcourses):
        super().__init__(name, address)
        self.__course = []
    def addcourse(course):
        if course in self.__course:
            return (false)
        else:
            return (rrue)
    def removecourse(course):
        for c in self.course:
            if c==course:
                return(false)
            else:
                return(true)
    def tostring(self):
        return("Teacher:" +super().getaddress())

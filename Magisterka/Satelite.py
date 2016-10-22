from math import sqrt
import User
# tworzenie satelitow
class Satelite():

    def __init__(self, length, width, usr):
        self.__length = length
        self.__width = width
        self.__height = 20200  # km
        self.user = usr
        self.spr = self.odlSatUser()

        
    def getLenSat(self):
        return self.__length * 463.87  # dlugosc jednego stopnia na wysokosci 20200km  
    def getWidthSat(self):
        return self.__width * 463.87
    def getHeightSat(self):
        return self.__height
    def odlSatUser(self):
        R=sqrt(pow((self.user.getWidthUser()-self.getWidthSat()),2)
               +pow((self.user.getLenUser()-self.getLenSat()),2))
        return R
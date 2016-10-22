#klasa do tworzenia obiektu uzytkownika
import Bledy
import Satelite
class User(object):

    def __init__(self, length,width):
        self.__length=length
        self.__width=width
        self.__height=1
        
        
    def getLenUser(self):
        return self.__length*111.196672
    def getWidthUser(self):
        return self.__width*111.196672
    def getHeiUser(self):
        return self.__height
#klasa do obliczania bledow GPS 
from random import uniform
import os
class Bledy(object):
    def __init__(self, user,percent,plik):
        self.percent=percent
        self.user = user
        self.heightJ = 0
        self.widthJ = 0
        self.lenghtJ = 0
        self.widthU = user.getWidthUser()
        self.lenghtU = user.getLenUser()
        self.nazwaPliku=plik
        self.myfile = open(plik, "a")
        self.wszystkieBledy=[]
        self.count = {"efemeryd": 0,
                    "jonosfera": 0,
                    "troposfera": 0,
                    "wielodrogowosc": 0,
                    "instrumental": 0,
                    "zegar": 0,
                   }
        self.dict={"efemeryd": [],
                    "jonosfera": [],
                    "troposfera": [],
                    "wielodrogowosc": [],
                    "instrumental": [],
                    "zegar": [],
                    "DOP":[],
                   }
    def bladJonoDod(self):
        if(self.count["jonosfera"]==1):
            self.clean()
        self.count["jonosfera"] += 1
        tmpLen= (uniform(-12, 12))/1000
        tmpWidth= (uniform(-12, 12))/1000 
        self.lenghtJ += tmpLen
        self.widthJ += tmpWidth
        self.lenghtU+=tmpLen
        self.widthU+=tmpWidth
        print('Blad Jonosferyczny' + '\nwysokosc: ' + str(self.heightJ+self.user.getHeiUser()) + '\n'
                          'szerokosc: ' + str((self.widthJ+self.user.getWidthUser()) / 111.196672) + '\n'
                          'dlugosc: ' + str((self.lenghtJ+self.user.getLenUser()) / 111.196672) + '\n')
        self.dict["jonosfera"].append((self.widthJ+self.user.getWidthUser() / 111.196672))
        self.dict["jonosfera"].append((self.lenghtJ+self.user.getLenUser() / 111.196672))

    def bladTropoDod(self):
        if(self.count["troposfera"]==1):
            self.clean()
        self.count["troposfera"] += 1
        tmpLen= (uniform(-3, 3))/1000
        tmpWidth= (uniform(-3, 3))/1000 
        self.lenghtJ += tmpLen
        self.widthJ += tmpWidth
        self.lenghtU+=tmpLen
        self.widthU+=tmpWidth
        print('Blad Troposferyczny' + '\nwysokosc: ' + str(self.heightJ+self.user.getHeiUser()) + '\n'
                          'szerokosc: ' + str((self.widthJ+self.user.getWidthUser()) / 111.196672) + '\n'
                          'dlugosc: ' + str((self.lenghtJ+self.user.getLenUser()) / 111.196672) + '\n\n')
        self.dict["troposfera"].append(self.widthJ+self.user.getWidthUser() / 111.196672)
        self.dict["troposfera"].append(self.lenghtJ+self.user.getLenUser() / 111.196672)
        
    def bladEfemerydDod(self):# roznica miedzy polozeniem satelity wyliczonym z danych orbitalnych, a rzeczywistym

        if(self.count["efemeryd"]==1):
            self.clean()
        self.count["efemeryd"] += 1
        tmpLen= (uniform(-40, 40))/1000
        tmpWidth= (uniform(-40, 40))/1000 
        self.lenghtJ += tmpLen
        self.widthJ += tmpWidth
        self.lenghtU+=tmpLen
        self.widthU+=tmpWidth
        print('Blad Efemeryd' + '\nwysokosc: ' + str(self.heightJ+self.user.getHeiUser()) + '\n'
                          'szerokosc: ' + str((self.widthJ+self.user.getWidthUser()) / 111.196672) + '\n'
                          'dlugosc: ' + str((self.lenghtJ+self.user.getLenUser()) / 111.196672) + '\n\n')
        self.dict["efemeryd"].append(self.widthJ+self.user.getWidthUser() / 111.196672)
        self.dict["efemeryd"].append(self.lenghtJ+self.user.getLenUser() / 111.196672)        
 
    def bladZegaraDod(self):
        if(self.count["zegar"]==1):
            self.clean()
        self.count["zegar"] += 1
        tmpLen= (uniform(-15, 15))/1000
        tmpWidth= (uniform(-15, 15))/1000 
        self.lenghtJ += tmpLen
        self.widthJ += tmpWidth
        self.lenghtU+=tmpLen
        self.widthU+=tmpWidth
        print('Blad Zegara' + '\nwysokosc: ' + str(self.heightJ+self.user.getHeiUser()) + '\n'
                          'szerokosc: ' + str((self.widthJ+self.user.getWidthUser()) / 111.196672) + '\n'
                          'dlugosc: ' + str((self.lenghtJ+self.user.getLenUser()) / 111.196672) + '\n\n')
        self.dict["zegar"].append(self.widthJ+self.user.getWidthUser() / 111.196672)
        self.dict["zegar"].append(self.lenghtJ+self.user.getLenUser() / 111.196672)      

    def bladInstrtumentDod(self):
        if(self.count["instrumental"]==1):
            self.clean()
        self.count["instrumental"] += 1
        tmpLen= (uniform(-1, 1))/1000
        tmpWidth= (uniform(-1, 1))/1000 
        self.lenghtJ += tmpLen
        self.widthJ += tmpWidth
        self.lenghtU+=tmpLen
        self.widthU+=tmpWidth
        print('Blad Instrumentalny' + '\nwysokosc: ' + str(self.heightJ+self.user.getHeiUser()) + '\n'
                          'szerokosc: ' + str((self.widthJ+self.user.getWidthUser()) / 111.196672) + '\n'
                          'dlugosc: ' + str((self.lenghtJ+self.user.getLenUser()) / 111.196672) + '\n\n')
        self.dict["instrumental"].append(self.widthJ+self.user.getWidthUser() / 111.196672)
        self.dict["instrumental"].append(self.lenghtJ+self.user.getLenUser() / 111.196672)       
   
    def bladWielodrogDod(self):
        if(self.count["wielodrogowosc"]==1):
            self.clean()
        self.count["wielodrogowosc"] += 1
        tmpLen= (uniform(-2, 2))/1000
        tmpWidth= (uniform(-2, 2))/1000 
        self.lenghtJ += tmpLen
        self.widthJ += tmpWidth
        self.lenghtU+=tmpLen
        self.widthU+=tmpWidth
        print('Blad Wielodrogowosci' + '\nwysokosc: ' + str(self.heightJ+self.user.getHeiUser()) + '\n'
                          'szerokosc: ' + str((self.widthJ+self.user.getWidthUser()) / 111.196672) + '\n'
                          'dlugosc: ' + str((self.lenghtJ+self.user.getLenUser()) / 111.196672) + '\n\n')
        self.dict["wielodrogowosc"].append((self.widthJ+self.user.getWidthUser()) / 111.196672)
        self.dict["wielodrogowosc"].append((self.lenghtJ+self.user.getLenUser()) / 111.196672)     

    def DOP(self):#blad przez niedogodne polozenie satelitow wyrazone w procentach od glownego bledu
        self.lenghtU*=(1.0+self.percent.percent)
        self.widthU*=(1.0+self.percent.percent)
        self.lenghtJ*=(1.0+self.percent.percent)
        self.widthJ*=(1.0+self.percent.percent)
        print('Wplyw ustawienia satelitow' + '\nwysokosc: ' + str(self.heightJ+self.user.getHeiUser()) + '\n'
                          'szerokosc: ' + str((self.widthJ+self.user.getWidthUser()) / 111.196672) + '\n'
                          'dlugosc: ' + str((self.lenghtJ+self.user.getLenUser()) / 111.196672) + '\n')
        self.dict["DOP"].append((self.widthJ+self.user.getWidthUser()) / 111.196672)
        self.dict["DOP"].append((self.lenghtJ+self.user.getLenUser()) / 111.196672)
        self.zapisDoPliku()

    def clean(self):#czyszczenie gdy byl blad juz wywolany
        self.lenghtJ=0
        self.widthJ=0
    
    def zapisDoPliku(self):
        try:
            for i in self.dict.values():
                for q in i:
                    self.wszystkieBledy.append(q)
                    self.myfile.write(str(q)+' ')
                self.myfile.write('\n')
            self.myfile.write('\n')
            self.myfile.close()
        except ValueError:
            self.myfile= open(self.nazwaPliku, "a")
            for i in self.dict.values():
                for q in i:
                    #self.liczbyDoPliku.append(str(q))
                    self.wszystkieBledy.append(q)
                    self.myfile.write(str(q)+' ')
                self.myfile.write('\n')
            self.myfile.write('\n')
            self.myfile.close()
    def usuwaniePliku(self,plik):
        if os.path.isfile(plik) :
            os.unlink(plik)
    def getGaussBledy(self):
        return self.wszystkieBledy
    def getGaussOstateczneBledy(self):
        return self.ostateczneBledy
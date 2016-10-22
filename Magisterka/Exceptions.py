import re
from math import fabs
from __builtin__ import True
# klasa dla funkcji by wyrzucac wyjatki
           
class Exceptions(object):
    def __init__(self):
        self.liczba = 0.0
        self.polkolaUSR = []
        self.polkolaSAT = []
    def liczby(self, dlgSzer):  # podawanie liczby dla uzytkownika
        try:
            wspl = KtoraPolkola(raw_input("podaj liczbe i oznaczenie polkuli oddzielone spacja przyklad (22.8 E) "))
            if(dlgSzer == 0):
                podzial = wspl.podzialWE(2, 0)
            elif(dlgSzer == 1):
                podzial = wspl.podzialNS(2, 0)    
            self.liczba = float(podzial[0])
            self.polkolaUSR.append(podzial[1])
            if(self.liczba > 180.0 or self.liczba < 0.0):
                print("liczba nie miesci sie w przedziale <0,180>")
                self.liczba = self.liczby()
        except ValueError:
            print("zly format przyklad (22.8 E)")
            self.liczba = self.liczby()
        except IndexError:
            print("zly format przyklad (22.8 E)")
            self.liczba = self.liczby()
        return self.liczba
    
    def liczbySatX(self, userX):  # podawanie liczby dla satelitow
        spr = True
        userX /= 111.196672
        
        while(spr):
            try:
                wspl = KtoraPolkola(raw_input("podaj liczbe i oznaczenie polkuli oddzielone spacja "))
                podzial = wspl.podzialWE(0, userX)
                self.liczba = float(podzial[0])
                if(self.liczba < 180 and self.liczba > 0):  # 35256,34 lub 53.74stopnie jest to odleglosc jaka moze byc maksymalna miedzy satelitami przy dalszej widocznosci uzytkownika
                    if(userX + 53.74 > 180.0):  # czy zakres wychodzi na druga polkole od 180
                        nowyUsr = fabs(((userX + 53.74) - 180) - 180)
                        if(podzial[1] == self.polkolaUSR[len(self.polkolaUSR) - 2]):  # czy ta sama polkola
                            if(self.liczba >= userX - 53.74 and self.liczba <= userX + 53.74):  # potrzebujemy tylko ograniczenia dolnego poniewaz gorne 180 zostalo wczesniej sprawdzone
                                print "wprowadziles prawidlowe dane"
                                spr = False
                        else:
                            if(self.liczba >= nowyUsr and self.liczba <= 180):
                                print "wprowadziles prawidlowe dane"
                                spr = False
                    elif(userX - 53.74 < 0):
                        nowyUsr = fabs(userX - 53.74)
                        if(podzial[1] == self.polkolaUSR[len(self.polkolaUSR) - 2]):  # czy ta sama polkola
                            if(self.liczba >= 0 and self.liczba <= userX + 53.74):  # potrzebujemy tylko ograniczenia dolnego poniewaz gorne 180 zostalo wczesniej sprawdzone
                                print "wprowadziles prawidlowe dane"
                                spr = False
                        else:
                            if(self.liczba >= 0 and self.liczba <= nowyUsr):
                                print "wprowadziles prawidlowe dane"
                                spr = False
                    elif(self.liczba >= userX - 53.74 and self.liczba < userX + 53.74):
                        print "wprowadziles prawidlowe dane"
                        spr = False
                    else:
                        print("liczba nie miesci sie w przedziale <0,180> lub satelita nie widzi uzytkownika przedzial: " + str(userX) + " +/- 53.74")
                        spr = True
                else:
                    print("liczba nie miesci sie w przedziale <0,180>")
                    spr = False
            except ValueError:
                print("to nie jest liczba")
                spr = True
            except IndexError:
                print("zly format przyklad (22.8 E)")
                spr = True
        self.polkolaSAT.append(podzial[1])
        return self.liczba
    
    def liczbySatY(self, userY):  # podawanie liczby dla satelitow
        spr = True
        userY /= 111.196672
        
        while(spr):
            try:
                wspl = KtoraPolkola(raw_input("podaj liczbe i oznaczenie polkuli oddzielone spacja "))
                podzial = wspl.podzialNS(0, userY)
                self.liczba = float(podzial[0])
                spr = True        
                if(self.liczba < 180 and self.liczba > 0):  # 35256,34 lub 53.74stopnie jest to odleglosc jaka moze byc maksymalna miedzy satelitami przy dalszej widocznosci uzytkownika
                    if(userY + 53.74 > 180.0):  # czy zakres wychodzi na druga polkole od 180
                        nowyUsr = fabs(((userY + 53.74) - 180) - 180)
                        if(podzial[1] == self.polkolaUSR[len(self.polkolaUSR) - 1]):  # czy ta sama polkola
                            if(self.liczba >= userY - 53.74 and self.liczba <= userY + 53.74):  # potrzebujemy tylko ograniczenia dolnego poniewaz gorne 180 zostalo wczesniej sprawdzone
                                print "wprowadziles prawidlowe dane"
                                spr = False
                        else:
                            if(self.liczba >= nowyUsr and self.liczba <= 180):
                                print "wprowadziles prawidlowe dane"
                                spr = False       
                    elif(userY - 53.74 < 0):
                        nowyUsr = fabs(userY + 53.74)
                        if(podzial[1] == self.polkolaUSR[len(self.polkolaUSR) - 1]):  # czy ta sama polkola
                            if(self.liczba >= 0 and self.liczba <= userY + 53.74):  # potrzebujemy tylko ograniczenia dolnego poniewaz gorne 180 zostalo wczesniej sprawdzone
                                print "wprowadziles prawidlowe dane"
                                spr = False
                        else:
                            if(self.liczba >= 0 and self.liczba <= nowyUsr):
                                print "wprowadziles prawidlowe dane"
                                spr = False
                    elif(self.liczba >= userY - 53.74 and self.liczba < userY + 53.74):
                        print "wprowadziles prawidlowe dane"
                        spr = False
                    else:
                        print("liczba nie miesci sie w przedziale <0,180> lub satelita nie widzi uzytkownika przedzial: " + str(userY) + " +/- 53.74")
                        spr = True
                else:
                    print("liczba nie miesci sie w przedziale <0,180>")
                    spr = False
            except ValueError:
                print("to nie jest liczba")
                self.liczba = self.liczbySatY(userY)()
            except IndexError:
                print("zly format przyklad (22.8 E)")
                self.liczba = self.liczbySatY(userY) 
        self.polkolaSAT.append(podzial[1])
        return self.liczba

    def pozaZasieg(self, a, usr, x, polkola):
        spr = True
        if(usr + 53.74 > 180):  # czy zakres wychodzi na druga polkole
            nowyUsr = 180 - (usr - 53.74)
            if(polkola == self.polkolaUSR[len(self.polkolaUSR) - 1]):  # czy ta sama polkola
                if(self.liczba >= usr - 53.74):  # potrzebujemy tylko ograniczenia dolnego poniewaz gorne 180 zostalo wczesniej sprawdzone
                    if(x == 1):
                        self.liczbySatY(usr)
                    else:
                        self.liczbySatX(usr)
            else:
                if(self.liczba <= 180 and self.liczba >= nowyUsr):
                    if(x == 1):
                        self.liczbySatY(usr)
                    else:
                        self.liczbySatX(usr)
        elif(usr < 53.74):  # czy zakres wychodzi na druga polkole
            nowyUsr = usr + 53.74
            if(polkola == self.polkolaUSR[len(self.polkolaUSR) - 1]):  # czy ta sama polkola
                if(self.liczba <= usr + 53.74 or self.liczba):  # potrzebujemy tylko ograniczenia dolnego poniewaz gorne 180 zostalo wczesniej sprawdzone
                    if(x == 1):
                        self.liczbySatY(usr)
                    else:
                        self.liczbySatX(usr)
            else:
                if(self.liczba >= 0 and self.liczba <= nowyUsr):
                    if(x == 1):
                        self.liczbySatY(usr)
                    else:
                        self.liczbySatX(usr)
        else:
            if(self.liczba > 53.74 + usr or self.liczba > 53.74 - usr):
                if(x == 1):
                    self.liczbySatY(usr)
                else:
                    self.liczbySatX(usr)
    def plik(self, nazwa):
        pattern = r"[a-z]*\.txt$"
        spr = True
        check = re.match(pattern, nazwa)
        if check:
            return nazwa
        else:
            print "podana nazwa posiada zly format"
            while(spr):
                self.calyTekst = raw_input("podaj nazwe pliku do wynikow przyklad (nazwa.txt) ")
                check = re.match(pattern, self.calyTekst) 
                if check:
                    spr = False
                if spr:
                    print "podana nazwa posiada zly format"
            return nazwa
        
    def wyborOpcji(self):
        tmpCheck = True
        while(tmpCheck):
            try:
                x1 = input('blad: \n1-Efemeryd \n2-Zegara \n3-Jonosferyczny' + 
                            '\n4-Troposferyczny \n5-Wielodrogowosci' + 
                            '\n6-Instrumentalny \n7-wszystkie \n8-usuniecie pliku \n9-Metoda najmniejszych kwadratow' + 
                            '\n10-wyjscie ')
                if(x1 == 1 or x1 == 2 or x1 == 3 or x1 == 4 or x1 == 5 or x1 == 6 or x1 == 7 or x1 == 8 or x1 == 9 or x1 == 10):
                    tmpCheck = False
            except NameError:
                print "nieprawidlowe dane"
                print
                tmpCheck = True
        return x1
class KtoraPolkola(Exceptions, object):
    def __init__(self, wpis):
        super(KtoraPolkola, self).__init__()
        self.calyTekst = wpis
    def podzialWE(self, fun, usr):
        pattern = r"\d*\.?\d*\s[WE]$"
        spr = True
        check = re.match(pattern, self.calyTekst)
        if check:
            podzielony = self.calyTekst.split(' ')
            podzielony[0]=float(podzielony[0])
            podzielony[0]=round(podzielony[0],4)
            print podzielony
            return podzielony
        else:
            print "podana liczba posiada zly format"
            while(spr):
                self.calyTekst = raw_input("podaj liczbe i oznaczenie polkuli oddzielone spacja przyklad (22.8 E) ")
                check = re.match(pattern, self.calyTekst) 
                if check:
                    podzielony = self.calyTekst.split(' ')
                    podzielony[0]=float(podzielony[0])
                    podzielony[0]=round(podzielony[0],4)
                    print podzielony                    
                    spr = False
                if spr:
                    print "podana liczba posiada zly format"
            return podzielony
    def podzialNS(self, fun, usr):
        pattern = r"\d*\.?\d*\s[NS]$"
        spr = True
        check = re.match(pattern, self.calyTekst)
        if check:
            podzielony = self.calyTekst.split(' ')
            podzielony[0]=float(podzielony[0])
            podzielony[0]=round(podzielony[0],4)
            print podzielony
            return podzielony
        else:
            print "podana liczba posiada zly format"
            while(spr):
                self.calyTekst = raw_input("podaj liczbe i oznaczenie polkuli oddzielone spacja przyklad (22.8 E) ")
                check = re.match(pattern, self.calyTekst) 
                if check:
                    podzielony = self.calyTekst.split(' ')
                    podzielony[0]=float(podzielony[0])
                    podzielony[0]=round(podzielony[0],4)
                    print podzielony            
                    spr = False
                if spr:
                    print "podana liczba posiada zly format"
            print podzielony
            return podzielony
        
        

import Satelite
import User
import Bledy
import Procent
import Exceptions
import Gauss
import sys
if __name__ == '__main__':
    # dopoki uzytkownik nie postanowi zrezygnoac bedzie program dzialac
    check = 'uzytkownik'
    q = True
    
    while(q):
        
        exc = Exceptions.Exceptions()
        if(check.lower() == 'uzytkownik'):
            print("podaj dlugosc i szerokosc geograficzna uzytkownika uzywajac na koncu oznaczenia N/S/W/E")
            usr = User.User(exc.liczby(0), exc.liczby(1))
            

            print("podaj wspolrzedne pierwszego satelity (dlugosc i szerokosc)")
            sat1 = Satelite.Satelite(exc.liczbySatX(usr.getLenUser()), exc.liczbySatY(usr.getWidthUser()), usr)
            print("podaj wspolrzedne drugiego satelity (dlugosc i szerokosc)")
            sat2 = Satelite.Satelite(exc.liczbySatX(usr.getLenUser()), exc.liczbySatY(usr.getWidthUser()), usr)
            print("podaj wspolrzedne trzeciego satelity (dlugosc i szerokosc)")
            sat3 = Satelite.Satelite(exc.liczbySatX(usr.getLenUser()), exc.liczbySatY(usr.getWidthUser()), usr)
            print("podaj wspolrzedne czwartego satelity (dlugosc i szerokosc)")
            sat4 = Satelite.Satelite(exc.liczbySatX(usr.getLenUser()), exc.liczbySatY(usr.getWidthUser()), usr)
            proc = Procent.Procent(sat1, sat2, sat3, sat4)
            plik = exc.plik(raw_input("podaj nazwe pliku do wynikow (nazwa.txt) "))
            blad = Bledy.Bledy(usr, proc, plik)
        elif(check.lower() == 'satelity'):
            print("podaj wspolrzedne pierwszego satelity (dlugosc i szerokosc)")
            sat1 = Satelite.Satelite(exc.liczbySatX(usr.getLenUser()), exc.liczbySatY(usr.getWidthUser()), usr)
            print("podaj wspolrzedne drugiego satelity (dlugosc i szerokosc)")
            sat2 = Satelite.Satelite(exc.liczbySatX(usr.getLenUser()), exc.liczbySatY(usr.getWidthUser()), usr)
            print("podaj wspolrzedne trzeciego satelity (dlugosc i szerokosc)")
            sat3 = Satelite.Satelite(exc.liczbySatX(usr.getLenUser()), exc.liczbySatY(usr.getWidthUser()), usr)
            print("podaj wspolrzedne czwartego satelity (dlugosc i szerokosc)")
            sat4 = Satelite.Satelite(exc.liczbySatX(usr.getLenUser()), exc.liczbySatY(usr.getWidthUser()), usr)
            proc = Procent.Procent(sat1, sat2, sat3, sat4)
            blad = Bledy.Bledy(usr, proc)
        else:
            exit          
        gaussDlg = Gauss.Gauss(blad.getGaussBledy(), "dlugosc")
        gaussSzer = Gauss.Gauss(blad.getGaussBledy(), "szerokosc")
        p = True
        while(p == True):

            x1 = exc.wyborOpcji()

            if(x1 == 1):
                blad.bladEfemerydDod()
            elif(x1 == 2):
                blad.bladZegaraDod()
            elif(x1 == 3):
                blad.bladJonoDod()
            elif(x1 == 4):
                blad.bladTropoDod()
            elif(x1 == 5):
                blad.bladWielodrogDod()
            elif(x1 == 6):
                blad.bladInstrtumentDod()
            elif(x1 == 7):
                blad.bladEfemerydDod()
                blad.bladZegaraDod()
                blad.bladJonoDod()
                blad.bladTropoDod()
                blad.bladWielodrogDod()
                blad.bladInstrtumentDod()
                # blad.DOP()
            elif(x1 == 8):
                blad.usuwaniePliku(plik)
            elif(x1 == 9):
                blad.DOP()
                gaussDlg.parametrDlg()
                gaussDlg.wykres()
                gaussSzer.parametrSzer()
                gaussSzer.wykres()
                blad.wszystkieBledy = []
            else:
                blad.DOP()
                p = False
                q = False
                sys.exit()
               
            petla = True
            while(petla):
                check = raw_input("czy chcesz wyznaczyc nowe wspolrzedne uzytkownika i satelitow czy tylko satelitow czy przejsc do opcji? uzytkownik/satelitow/opcje ")
                if(check == "uzytkonik" or "satelity"):
                    petla = False
                    p = False
                elif(check == "opcje"):
                    petla = False
                    p = True
                else:
                    petla = True

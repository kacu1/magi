'''
Created on Jul 27, 2016

@author: Michal
'''
import Bledy
import numpy
import matplotlib
from pylab import *
import sympy
#wykres dla dlugosci, szerokosci i bledow
class Gauss(object):

    def __init__(self, bledy,nazwa):
        self.bledy=bledy#co drugi to dlugosc zaczynajac od pierwszego elementu
        self.y=[]
        self.x=0
        self.nazwa=nazwa #z czym tworzona jest funkcja dlugosc/szerokosc/calkowite
    def parametrDlg(self):
        self.x=len(self.bledy)/2
        for i in range(0,len(self.bledy),2):
            self.y.append(self.bledy[i])
    def parametrSzer(self):
        self.x=len(self.bledy)/2
        for i in range(1,len(self.bledy),2):
            self.y.append(self.bledy[i])
    def obliczeniaAB(self):
        self.x=len(self.y)
        a=0
        b=0
        c=0
        for i in range(0,self.x):
            a+=i*i
            b+=i
            c+=self.y[i]*i
        a1=0
        b1=0
        c1=0
        for i in range(0,self.x):
            a1+=i
            b1+=1
            c1+=self.y[i]
        A=array([[a,b],[a1,b1]])
        B=array([[c,c1]]).T
        AB=linalg.solve(A, B)
        return AB
    def wykres(self):
        AB=self.obliczeniaAB()
        osY=range(0,self.x)
        fun=[]
        for i in range(0,len(osY)):
            fun.append(AB[0]*osY[i]+AB[1])
        plot(osY,self.y, 'ro',osY,fun,'-')
        xlabel('ilosc bledow')
        ylabel('stopnie (o)')
        title('metoda najmnijszych kwadratow '+self.nazwa)
        grid(True)
        savefig("test.png")
        show()
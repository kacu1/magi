#klasa do wyliczania odleglosci miedzy satelitami 
from math import sqrt
import Satelite
class Procent(object):
    '''
    classdocs
    '''
    def __init__(self, sat1,sat2,sat3,sat4):
        self.sat1=sat1
        self.sat2=sat2
        self.sat3=sat3
        self.sat4=sat4
        self.s1s2=self.odlOdSat(self.sat1.getWidthSat(),self.sat2.getWidthSat(),
                      self.sat1.getLenSat(),self.sat2.getLenSat())
        self.s1s3=self.odlOdSat(self.sat1.getWidthSat(),self.sat3.getWidthSat(),
                      self.sat1.getLenSat(),self.sat3.getLenSat())
        self.s1s4=self.odlOdSat(self.sat1.getWidthSat(),self.sat4.getWidthSat(),
                      self.sat1.getLenSat(),self.sat4.getLenSat())
        self.s2s3=self.odlOdSat(self.sat2.getWidthSat(),self.sat3.getWidthSat(),
                      self.sat2.getLenSat(),self.sat3.getLenSat())
        self.s2s4=self.odlOdSat(self.sat2.getWidthSat(),self.sat4.getWidthSat(),
                      self.sat2.getLenSat(),self.sat4.getLenSat())
        self.s3s4=self.odlOdSat(self.sat3.getWidthSat(),self.sat4.getWidthSat(),
                      self.sat3.getLenSat(),self.sat4.getLenSat())
        self.percent=self.percent()
        
    def percent(self):#obliczanie procentu calkowitego na w stosunku do obleglosci miedzy satelitami
        bok=35256#odleglosc satelitow w kwadracie
        percent=0
         #35256 km to max odleglosci miedzy satelitami
        if(self.s1s2<bok):
            percent+=3.0*self.s1s2/bok
        if(self.s1s3<bok):
            percent+=3.0*self.s1s3/bok
        if(self.s1s4<bok):
            percent+=3.0*self.s1s4/bok
        if(self.s2s3<bok):
            percent+=3.0*self.s2s3/bok
        if(self.s2s4<bok):
            percent+=3.0*self.s2s4/bok
        if(self.s3s4<bok):
            percent+=3.0*self.s3s4/bok
        return percent
    
    def odlOdSat(self,x1,x2,y1,y2):
        R=sqrt(pow((x1-x2),2)+
               pow((y1-y2),2))
        return R
    

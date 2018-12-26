#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:05:25 2018
@author: enaut.genua
"""
import random
class Casilla:
    def __init__(self, posx, posy):
        self.x = int(posx) #Posición de la casilla en el eje x
        self.y = int(posy) #Posición de la casilla en el eje y
        self.lev = False #Estado de la casilla, True = levantado, False = Tapado
        self.val = random.randint(0, 4)#else = numero, 1 = mina.
    def get_pos(self):
        return self.x, self.y #Devuelve posición
    def get_lev(self):
       return self.lev#Devuelve el estado
    def set_lev(self, lev):
        self.lev = lev #Cambia de estado a la casilla 
    def get_val(self):  
        return self.val
class numero(Casilla):
    def __init__(self, posx, posy):
        Casilla.__init__(self, posx, posy)
        self.contador=int(0)
        self.val = 0
    def analizar_minas(self, matr):
        for i in range(max(self.x-1, 0), min(self.x+2, len(matr))):
            for j in range(max(self.y-1, 0), min(self.y+2, len(matr[0]))):
                if Casilla.get_val(matr[i][j]) == 1:
                    self.contador+=1
        return self.contador       
class mina(Casilla):
    def __init__(self, posx, posy):
        Casilla.__init__(self, posx, posy)
        self.val = 1
    def existe(self):
        return self.val
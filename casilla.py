#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:05:25 2018

@author: enaut
"""
import random
class Casilla:
    def __init__(self, posx, posy):
        self.x = int(posx) #Posición de la casilla en el eje x
        self.y = int(posy) #Posición de la casilla en el eje y
        self.lev = False #Estado de la casilla, True = levantado, False = Tapado
        a = random.randint(0,1)#0 = numero, 1 = mina.
        if a == 1:
            self.val = int(a)
        else:
            self.val = numero(self.x, self.y)
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
    def analizar_minas(self, matr):
        for dimx in range(self.x-1, self.x+1):
                for dimy in range(self.y-1, self.y+1):
                    if Casilla.get_val == 1:
                        self.contador+=1
    def get_valor(self):
        return self.contador        

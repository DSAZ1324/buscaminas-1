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
        self.val = random.randint(0,1)
    def get_pos(self):
        return self.x, self.y #Devuelve posición
    def get_lev(self):
       return self.lev#Devuelve el estado
    def set_lev(self, lev):
        self.lev = lev #Cambia de estado a la casilla
    #def set_val(self):  
     #   self.val = random.randint(0,1)  #Devuelve entero entre 0 y 2, 
#0 = numero, 1 = mina.
    def get_val(self):  
        return self.val

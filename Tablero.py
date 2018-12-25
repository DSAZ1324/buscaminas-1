# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:38:01 2018

@author: caper
"""
from casilla import Casilla
class Tablero:
    def __init__(self, i, j):
        self.i = int(i)
        self.j = int(j)
    def crear_tab(self):
        matr= []
        matraux = []
        for i in range(self.i):
            for j in range(self.j):
                if len(matraux) < self.j:
                    matraux.append(Casilla(i, j))
            matr.append(matraux)
            matraux = []
        return matr
    def levantar(self, matr):
        for x in range(self.i-1, self.i+1):
                for y in range(self.j-1, self.j+1):
                     matr[x][y] = Casilla(x, y)
                     val_casilla = Casilla.get_lev()
        return val_casilla            
            
        
        #Crear tablero aqui
        #Levantar funcion o metodo? (Recursivo) 

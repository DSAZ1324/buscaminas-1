#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:18:57 2018

@author: enaut
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
                    matraux.append(Casilla(i, j).get_val())
            matr.append(matraux)
            matraux = []
        return matr
    def levantar(self, matr):
        for dimx in range(self.i-1, self.i+1):
                for dimy in range(self.j-1, self.j+1):
                     matr[dimx[dimy]] = Casilla

        
        #Crear tabero aqui
        #Levantar funcion o metodo? (Recursivo) 
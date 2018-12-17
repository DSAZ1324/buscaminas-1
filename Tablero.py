#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:18:57 2018

@author: enaut
"""
import casilla
class Tablero:
    def __init__(self, i, j):
        self.i = int(i)
        self.j = int(j)
    def crear_tab(self):
        matr= []
        for i in range(self.i):
            for j in range(self.j):
                matr = matr[i[j]].append(Casilla.set_val())#Irá creando en cada casilla un objeto, repasar
        return matr
    def levantar(self, matr):
        for dimx in range(self.i-1, self.i+2):
                for dimy in range(self.j-1, self.j+2):
                    if Casilla.get_val == 1:
                        self.contador+=1

        
        #Crear tabero aqui
        #Levantar funcion o metodo? (Recursivo)
    
        
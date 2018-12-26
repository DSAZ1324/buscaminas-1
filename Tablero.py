# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:38:01 2018

@author: enaut.genua
"""
from casilla import Casilla
from casilla import numero
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
    
    
    
            
                            
                        
                        
                        
                    
        
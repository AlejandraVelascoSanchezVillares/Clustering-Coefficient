# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:43:29 2019

@author: jandr
"""
import numpy as np

data = open("routes_clean.dat", 'r')
contenu_data = data.read()
contenu_data = contenu_data.split("\n") #list on edge (['3646 3673', 3333 3673], ...)
print(contenu_data)

#for i in routes:
    #print (i)
    #Neighborhood = [];
    #if routes(i)
    #Neighborhood.append()
    #c(i)=e(i)/(deg(i)*(deg(i)-1)/2)
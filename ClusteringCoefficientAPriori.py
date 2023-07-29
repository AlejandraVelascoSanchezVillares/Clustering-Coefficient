# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:43:29 2019

@author: jandr
"""
import numpy as np

data = open("routes_clean.dat", 'r')
contenu_data = data.read()
contenu_data = contenu_data.split("\n") #list on edge (['3646 3673', 3333 3673], ...)
contenido_data = []
for i in range(len(contenu_data)):
    c = contenu_data[i].split(" ")
    contenido_data.append(c)
    
#print (contenido_data)
#print(contenu_data)

def find_numbers_of_neighbours (contenido_data):
    visited_nodes = []
    neighborhoods = []
    for i in range(len(contenido_data)):
        for j in range(2):
            current_node = contenido_data[i][j]
            neighbourhood = 0
            if current_node in visited_nodes:
                break
            else:
                visited_nodes.append(current_node)
                for k in range(len(contenido_data)):
                    if current_node in contenido_data[k]:
                        neighbourhood+=1
            neighborhoods.append(neighbourhood)
    return (neighborhoods)

numeritos = find_numbers_of_neighbours (contenido_data)

def find_neighbourhoods (contenido_data):
    visited_nodes = []
    neighborhoods = []
    for i in range(len(contenido_data)):
        for j in range(2):
            current_node = contenido_data[i][j]
            neighbourhood = []
            if current_node in visited_nodes:
                break
            else:
                visited_nodes.append(current_node)
                neighbourhood.append(current_node)
                for k in range(len(contenido_data)):
                    if current_node in contenido_data[k]:
                        for l in range(2):
                            if current_node == contenido_data[k][l]:
                                break
                            else:
                                neighbourhood.append(contenido_data[k][l])
            neighborhoods.append(neighbourhood)
    return (neighborhoods)

vecinitos = find_neighbourhoods(contenido_data)

def find_neighbourhoods_edges (vecinitos, contenido_data):
    neighbourhoods_edges = []
    for i in range(len(vecinitos)):
        neighbourhood_edges = 0
        for k in range(len(contenido_data)):
            if contenido_data[k][0] in vecinitos[i]:
                if contenido_data[k][1] in vecinitos[i]:
                    neighbourhood_edges += 1
        neighbourhoods_edges.append(neighbourhood_edges)
    return(neighbourhoods_edges)
    
aristas = find_neighbourhoods_edges (vecinitos, contenido_data)

c = 0

for v in range(len(vecinitos)):
    if (numeritos[v]*(numeritos[v]-1)/2)!=0:
        cv = aristas[v]/(numeritos[v]*(numeritos[v]-1)/2)
        c += cv
print(c/len(vecinitos))
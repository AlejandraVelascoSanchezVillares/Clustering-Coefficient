# -*- coding: utf-8 -*-

def determinante(M):
    c, M = triangular(M)
    return prod_diagonal(M) * c 

def triangular(M):
    c=1  # Tracks the symbol when swapping columns.
    N = len(M[0]);
    for i in range(N):
        for j in range(i+1,N):
            if (M[i][i]==0):   # have to swap
                M[i],M[j] = M[j],M[i]
                c=c*(-1);
            else:
                coef= - M[j][i]*1.0 / M[i][i]
                M[j]=suma(coef,M[i],M[j])
    return c,M


# Mi Ni are lists of N elements
def suma(coef,Mi,Ni):
    R=[0]*len(Mi)
    for i in range(len(Mi)):
        R[i]=Mi[i]*coef + Ni[i]
    return R

def prod_diagonal(M):
    a , N = 1 , len(M[0])
    for i in range(N):
        a = a * M[i][i]
    return a


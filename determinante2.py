# Credits to pupils suggesting this simpler approach.
def determinante(M):
    M = triangular(M)
    return prod_diagonal(M) 
    
#Simple version
def triangularSimple(M):
    c=1
    N = len(M[0]);
    for i in range(N):
        for j in range(i+1,N):
                M[j]=sumaV(M[j][i],M[i],M[i][i],M[j])
    return M

def sumaV(a,Mi,b,Mj):
    R=[0]*len(Mi)
    for k in range(len(Mi)):
        R[k] = a*Mi[k] - b*Mj[k]
    return R

def prod_diagonal(M):
    a , N = 1 , len(M[0])
    for i in range(N):
        a = a * M[i][i]
    return a

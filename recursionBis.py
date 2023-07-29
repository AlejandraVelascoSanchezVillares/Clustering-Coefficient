# Given b > 1 , and a > 0, give a function to
# provide log(b,a).
# Pre b > 1
def log(b,a):
    if (a<b) :
        return 0
    else:
        return 1 + log(b,a / b )

# Pre: len(v)>0
def capicua(v):
    return capicua_1(v,0,len(v)-1)

#empty not accepted
# inf <= sup
def capicua_1(v,inf, sup):
    if (inf==sup) :
        return True
    elif (inf+1==sup): #size 2.
        return v[inf]==v[sup]
    else:
        return (v[inf]==v[sup]) and capicua_1(v,inf+1,sup-1)
    
# More alla python in line.
# len(v)>= 1
def capicua_python(v):
    if (len(v)==1):
        return True
    elif (len(v)==2):
        return v[0]==v[-1]
    else:
        return (v[0]==v[-1]) and capicua_python(v[1:-1])

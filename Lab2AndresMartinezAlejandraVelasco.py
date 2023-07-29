"""
Created on Thu Feb 14 18:49:00 2019

@author: Andrés
"""

import numpy 
import random, math
from scipy.optimize import minimize
import matplotlib.pyplot as plt

global inputs

def kernel(x,y,typ):
    # Function computing the kernel for two datapoints with some type given
    if typ=='linear':
        k=numpy.inner(x,y)
        return k
    elif typ=='polynomial':
        #order=input('Enter polynomial order')
        k=(numpy.inner(x,y)+1)**order
        return k
    elif typ=='radial':
        #sigma=input('Enter sigma')
        k=numpy.exp(-numpy.linalg.norm(x-y)**2/(2*sigma**2))
        return k
    
def objective(alfa):
    # Implement equation 4
    summand=numpy.outer(alfa,alfa)*P
    a=numpy.sum(summand,axis=1)
    return 0.5*numpy.sum(a,axis=0)-numpy.sum(alfa)

def zerofun(alfa):
    # Implement constraint from Equation 10
    return numpy.sum(numpy.dot(alfa,targets))
    
def indicator(x,y):
    # Implement classification of point with coordinates (x,y)
    kernel_xy=numpy.zeros(len(targets))
    for i in range(len(targets)):
        kernel_xy[i]=kernel(inputs[i,:],[x,y],typ)
    return numpy.sum(numpy.multiply(aux,kernel_xy))-be
    
numpy.random.seed(100)   
classA = numpy.concatenate((numpy.random.randn(10,2) * 0.2 + [1.5,0.5] ,numpy.random.randn(10,2) * 0.2 + [-1.5 , 0.5 ]))
classB = numpy.random.randn(20,2) * 0.2 + [0.0 ,-0.5]
inputs = numpy.concatenate((classA , classB ))
global targets

targets = numpy.concatenate (
        (numpy.ones(classA.shape[0]) ,
         -numpy.ones(classB.shape[0])))
N = inputs.shape [0] # Number o f rows ( samples )
permute=list(range(N))
random.shuffle(permute)
inputs = inputs[permute,:]
targets = targets[permute]

typ='polynomial'
global order
order=2
global sigma
sigma=2
K=numpy.zeros([len(targets),len(targets)])
for i in range(len(targets)):
    for j in range(len(targets)):
        K[i,j]=kernel(inputs[i,:],inputs[j,:],typ)
print(K)        

global P
P=numpy.outer(targets,targets)*K

start=numpy.zeros(N) # Initial guess of alfa
C=10
B=[(0,C) for b in range(N)] # Bounds for minimize function
XC={'type':'eq', 'fun':zerofun} # Constraints for minimize function

ret = minimize(objective,start,
               bounds=B, constraints=XC)

alfa = ret['x']

# Obtain indices where alfa is non-zero (larger than 10^(-5))
pos=numpy.where(alfa>=10**(-5))
sv=inputs[pos,:]
t_sv=targets[pos]

# Compute b
global aux
global kernel_sv
global be
aux=numpy.outer(alfa,targets)
kernel_sv=numpy.zeros(len(targets))
for i in range(len(targets)):
    kernel_sv[i]=kernel(inputs[i,:],sv[0,0],typ)
    
be=numpy.sum(numpy.multiply(aux,kernel_sv))-t_sv[0]


# Apply Equation 6 to obtain the final output
#ind=numpy.sum(numpy.multiply(aux,kernel_sv))-be


# PLOTTING POINTS
plt.plot( [ p[0] for p in classA ], [ p[1] for p in classA ], 'b.')
plt.plot ( [ p[0] for p in classB ], [ p [1] for p in classB], 'r.')
plt.axis('equal') # Force same scale on both axes
plt.savefig('svmplot.pdf') # Save a copy in a file
plt.show ( ) # Show the plot on the screen

# PLOTTING DECISION BOUNDARY
global kernel_xy
xgrid = numpy.linspace(5, 5)
ygrid = numpy.linspace (4 , 4)
grid = numpy.array([[ indicator(x,y) for x in xgrid ] for y in ygrid])
plt.contour (xgrid, ygrid, grid, (-1.0, 0.0, 1.0), colors = ('red','black','blue'), linewidths = (1,3,1))
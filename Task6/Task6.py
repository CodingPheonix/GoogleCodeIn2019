import time
import numpy as np
from random import *
import matplotlib
import matplotlib.pyplot as plt

npdata = []
pydata = []

fig, ax = plt.subplots()

for i in range(50):
    start = time.time()
    np.dot(np.random.randint(6, size=(5*(i+1),5*(i+1))),np.random.randint(6, size=(5*(i+1),5*(i+1))))
    end = time.time()
    npdata.append([5*(i+1), end-start])

for i in range(50):
        
    start = time.time()
    
    X = [[int(random()*6) for j in range(5*(i+1))] for k in range(5*(i+1))]
    Y = [[int(random()*6) for j in range(5*(i+1))] for k in range(5*(i+1))]
    
    [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    
    end = time.time()
    pydata.append([5*(i+1), end-start])
    
pyPlt, = plt.plot(*zip(*pydata), label='Python')
npPlt, = plt.plot(*zip(*npdata), label='Numpy')
plt.legend([pyPlt, npPlt], ['Python', 'Numpy'])


ax.set(xlabel='Size of matricies', ylabel='Time taken in seconds',
       title='Python vs. Numpy:\nMultiplying matricies')
ax.grid()

plt.show()

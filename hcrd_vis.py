from functions import *
import matplotlib.pyplot as plt 
import numpy as np
import cmath
import time as t

x = np.linspace(-1.5,2,1000)
y = np.linspace(-1.5,1.5,1000)*1j

start = t.time_ns()
c = np.array([[i+j for i in x] for j in y])
#print(c)

znext = lambda z, c: z**2 + c

def perform_iter (func, seed,n = 200, delta = 10):
    prev = 0 + 0j
    changes = []
    for i in range(n):
        prev = func(prev, seed)
        if np.isnan(abs(prev)):
            return False
    return not (abs(prev) > delta)


temp = []
for row in c:
    for item in row:
        if abs(item)<1.5 and perform_iter(znext, item):
            temp.append(item)

#print(temp)
x = [i.real for i in temp]
y = [i.imag for i in temp]
# print(y)

print((t.time_ns() - start)/10**9 )
fig,ax = plt.subplots(1,1,figsize = (14,14))

ax.scatter(x,y, s = .7, color = "#3A507D")
ax.grid(False)
ax.axis('off')
plt.savefig("MandleBrot.png")
#ax.set_ylim([-10,10])
plt.show()

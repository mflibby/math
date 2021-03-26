import integration as i
import numpy as np
import functions as func
import matplotlib.pyplot as plt
import linear_algebra as lin
from riemann import *


x = np.arange(1,10000)
y = []
s = .5+14.135j
full = func.ζlist(s, range(1,10000))
avgs = []
avgs2 = []
avgs3 = []
avgs4 = []
avgs5 = []
for i in x:
    y.append(sum(full[0:i]))
    avgs.append(func.avg(y))
    avgs2.append(func.avg(avgs))
    avgs3.append(func.avg(avgs2))
    avgs4.append(func.avg(avgs3))
    avgs5.append(func.avg(avgs4))

#fig = plt.figure(figsize=(14,14))
#ax = fig.add_subplot(111, projection='3d')

fig,ax = plt.subplots(1,1, figsize=(10,10))
#plot_3d(x,y,[avgs5],ax)
#ax.plot([0,10000],[avg(avgs5).real,avg(avgs5).real],[avg(avgs5).imag,avg(avgs5).imag],color="BLACK")
#print(avg(avgs),avg(avgs4),avg(avgs5))
#plot_3dsinusoid(lambda x : s.imag*np.log(x), "\ln(x)", np.linspace(1,10000,100000),ax, (lambda x: np.sqrt(x)/s.imag)(np.linspace(1,10000,100000)))
#plot_terms2d(s,x,ax)
plot_terms2d(s+1,x,ax)
#plot_terms2d(s+4.135j,x,ax)
ax.grid()
plt.legend()
plt.show()

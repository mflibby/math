import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functions import *


def plot_2d(y, avgs):
    fig,ax = plt.subplots(1,1, figsize=(10,10))
    ax.scatter(x,np.sqrt(x)/14.135,s=.1)
    ax.scatter(x,[i.imag for i in y],s=.1, label = r"$Im(y)$")
    ax.scatter(x,[i.real for i in y],s=.1, label = r"$Re(y)$")
    for j in enumerate(avgs):
        ax.scatter(x,[i.real for i in j[1]],s=.1, label = f"$Im(avgs{j[0]})$")
        ax.scatter(x,[i.imag for i in j[1]],s=.1, label = f"$Im(avgs{j[0]})$")
        plt.scatter(x,[abs(i) for i in j[1]],s=.1, label = f"$Abs(avgs{j[0]})$")
    plt.scatter(x,[abs(i) for i in y],s=.1, label = r"$Abs(y)$")
    ax.grid()
    ax.legend(markerscale =40)
    plt.show()



def plot_3d(x,y,avgs,ax):


    ax.plot(x,[i.real for i in y], [i.imag for i in y])
    ax.plot(x,[abs(i) for i in y])
    for j in enumerate(avgs):
        ax.scatter(x,[i.real for i in j[1]],[i.imag for i in j[1]],s=.1, label = f"$Im(avgs{j[0]})$")
        ax.scatter(x,[abs(i) for i in j[1]],s=.1, label = f"$Abs(avgs{j[0]})$")

def plot_3dsinusoid(funcx, func_label, x,ax, mult=1):

    y1 = mult*np.sin(funcx(x))
    y2 = mult*np.cos(funcx(x))
    ax.plot(x,y1,y2, label = f'$f(x)=\sin({func_label})$')
    #ax.plot(x,y1+y2, label = f'$f(x)=\cos ({func_label})+\sin({func_label})$')
    #ax.plot(x,y1**2+y2**2, label = f'$f(x)=\cos ({func_label})^2+\sin({func_label})^2$')
    #ax.plot(x,mult)

def plot_terms2d(s,bound,ax):

    y = ζlist(s, bound)

    ax.plot(bound,[i.real for i in y], label = f"Re(s)={s}")
    ax.plot(bound,[i.imag for i in y], label = f"Im(s)={s}")

from functions import *
import matplotlib.pyplot as plt 
import numpy as np
import cmath
import time as t

x = np.linspace(-1.5,1.5,1000)
y = np.linspace(-1.5,1.5,1000)*1j

# start = t.time_ns()
class MandelBrot:

    def __init__(self, xlims= (-1.5,1.5), ylims=(-1.5,1.5),resolution = 1000):
        self.x = np.linspace(xlims[0],xlims[1],resolution)
        self.y = np.linspace(ylims[0],ylims[1],resolution)*1j

        self.c = np.array([[i+j for i in x] for j in y])
        # print(f"Complex field generated in {(t.time_ns() - start)/10**9}s...")

        self.znext = lambda z, c: z**2 + c

    def perform_iter (self, seed, n = 10, delta = 1.5):
        prev = 0 + 0j
        for _ in range(n):
            prev = self.znext(prev, seed)
            if np.isnan(abs(prev)) or abs(prev) > delta:
                return False
        return not (abs(prev) > delta)

    def run_animate (self, n_range, step = 1):
        for n in range(n_range[0], n_range[1]+1, step):
            self.run( n )

    def run(self, n = 100 ):
        temp = []
        for row in self.c:
            for item in row:
                if self.perform_iter(item,n):
                    temp.append(item)

        print(f"Mandel brot generated {n}...")
        #print(temp)
        x = [i.real for i in temp]
        y = [i.imag for i in temp]
        # print(y)

        # print((t.time_ns() - start)/10**9 )
        fig,ax = plt.subplots(1,1,figsize = (14,14))

        ax.scatter(x,y, s = .1, color = "#3A507D")
        ax.grid(False)
        ax.axis('off')
        plt.savefig(f"brots\MandleBrot_{n}.png")
        # plt.show()

brot = MandelBrot()

brot.run_animate([5,20])

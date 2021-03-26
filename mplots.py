import numpy as np

from bokeh.layouts import row, column
from bokeh.models import CustomJS, Slider
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.io import output_notebook
import integration as i

import functions as func
import linear_algebra as lin
from riemann import *

# Normal Distribution

#hist, edges = np.histogram(reducedlist(RZ,r_err,z_err,r_err_hist,z_err_hist, 0.5), bins=10000)
s = .5+14.135j
y = func.ζlist(s, range(1,1000))
source = ColumnDataSource(data=dict(x=np.arange(1,1000), y1=[i.real for i in y], y2 = [i.imag for i in y]))
ylist = [func.ζlist(0.5+i*1.0j, range(1,1000)) for i in np.arange(0,20,.01)]
termsreal = []
termsimag = []
for i in ylist:
    termsreal.append([j.real for j in i])
    termsimag.append([j.imag for j in i])
#print(termsreal[0])
p = figure(title='Rmag-Zmag', background_fill_color="#fafafa", x_range=(0, 1000), y_range=(-1, 1))
#p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
 #          fill_color="navy", line_color="black", alpha=1)
real = p.circle(x = 'x', y = 'y1', source = source, color = 'blue', size=1, alpha=0.5)
imag = p.circle(x = 'x', y = 'y2', source = source, color = 'red',size=1, alpha=0.5)



# Slider to select the binwidth, value is selected number
reduce_slider = Slider(start =0, end = 20,
                     step = 0.01, value = 14.13,
                     title = 'Im(s)')
#print('hello', reduce_slider.value)

callback = CustomJS(args=dict(source=source, reduce = reduce_slider, valsreal = termsreal, valsimag = termsimag),
                    code="""
    const index = reduce.value*100;
    source.data['y1'] = valsreal[index];
    source.data['y2'] = valsimag[index];


    source.change.emit();
""")

reduce_slider.js_on_change('value', callback)

layout = row(
    p,
    column(reduce_slider),
)

output_file('Reimann_Vis.html', title="Zeta Terms Visualization")
show(layout)

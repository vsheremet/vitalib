# -*- coding: utf-8 -*-
"""
test interpolation function

used for interpolating gps drifter data 
from nonuniform sampling to uniform 1h data
and for filling small gaps in the data

@author: Vitalii Sheremet
"""

import numpy as np
import matplotlib.pyplot as plt
from sh_interp3 import sh_interp3
#from vitalib import sh_interp3

# generate a sine wave on a nonuniform grid
L=3.*np.pi
t=np.random.rand(20)*L
t[0]=0.
t[-1]=L
t=np.sort(t)
f=np.sin(t)
# interpolate data to a regular grid
ti=np.arange(0.,L,0.1)
fi=sh_interp3(ti,t,f)
# exact sine wave on a finer grid
tt=np.arange(0.,L,0.001)
ff=np.sin(tt)

plt.figure(1)
plt.plot(tt,ff,'g-')
plt.plot(t,f,'bo-')
plt.plot(ti,fi,'r.-')
plt.legend(['exact','raw','interpolated'])
plt.show()

# Same as above but now introduce a gap in data 
# extend data to the second segment and interpolate within the gap
G=2.*np.pi*0.3 # gap
t2=t+L+G
t=np.concatenate((t, t2), axis=0)
f=np.sin(t)
ti=np.arange(0.,2*L+G,0.1)
fi=sh_interp3(ti,t,f)
tt=np.arange(0.,2*L+G,0.001)
ff=np.sin(tt)

plt.figure(2)
plt.plot(tt,ff,'g-')
plt.plot(t,f,'bo-')
plt.plot(ti,fi,'r.-')
plt.legend(['exact','raw','interpolated'])
plt.show()

#################################
# Filling a gap on a uniform grid 
# This illustrates how the gap width affects the quality of interpolation
# For gaps longer than 1/3 of the period errors become significant
#################################
# data on the first segment on uniform grid
t=np.arange(0,L+0.1,0.1)
f=np.sin(t)
ti=np.arange(0.,L,0.1)
fi=sh_interp3(ti,t,f)
tt=np.arange(0.,L,0.001)
ff=np.sin(tt)

plt.figure(3)
plt.plot(tt,ff,'g-')
plt.plot(t,f,'bo-')
plt.plot(ti,fi,'r.-')
plt.legend(['exact','raw','interpolated'])
plt.show()

# extend data to the second segment
# interpolate within the gap
t2=t+L+G
t=np.concatenate((t, t2), axis=0)
f=np.sin(t)
ti=np.arange(0.,2*L+G,0.1)
fi=sh_interp3(ti,t,f)
tt=np.arange(0.,2*L+G,0.001)
ff=np.sin(tt)

plt.figure(4)
plt.plot(tt,ff,'g-')
plt.plot(t,f,'bo-')
plt.plot(ti,fi,'r.-')
plt.legend(['exact','raw','interpolated'])
plt.show()

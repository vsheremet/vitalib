# -*- coding: utf-8 -*-
# NOAA NOS CO-OPS tidal data
# get six minute verified data
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

import requests

# sample opendap request
#URL1='http://opendap.co-ops.nos.noaa.gov/dods/IOOS/SixMin_Verified_Water_Level.ascii?WATERLEVEL_6MIN_VFD_PX.DATE_TIME,WATERLEVEL_6MIN_VFD_PX.WL_VALUE&WATERLEVEL_6MIN_VFD_PX._STATION_ID="8447930"&WATERLEVEL_6MIN_VFD_PX._DATUM="STND"&WATERLEVEL_6MIN_VFD_PX._BEGIN_DATE="20140301 00:00"&WATERLEVEL_6MIN_VFD_PX._END_DATE="20140331 00:00"'
#f=requests.get(URL1)
#f.text

# select station id, datum, and range of dates
STID='"8447930"' # Woods Hole
DATUM='"STND"'
t1=datetime(2013,1,1)
t2=datetime(2013,3,31)

# SixMin data can be requested in chunks less than 1 month - make multiple requests and append results
t=np.array([])
h=np.array([])

tt=np.arange(t1,t2,timedelta(days=30)).astype(datetime)
NChunks=len(tt)
tt=np.append(tt,t2)
for k in range(NChunks):
    #T1='"20140201 00:00"'
    #T2='"20140331 23:59"'
    T1=datetime.strftime(tt[k],'"%Y%m%d %H:%M"')
    T2=datetime.strftime(tt[k+1]-timedelta(minutes=1),'"%Y%m%d %H:%M"')
    print T1,T2

    URL='http://opendap.co-ops.nos.noaa.gov/dods/IOOS/SixMin_Verified_Water_Level.ascii?WATERLEVEL_6MIN_VFD_PX.DATE_TIME,WATERLEVEL_6MIN_VFD_PX.WL_VALUE&WATERLEVEL_6MIN_VFD_PX._STATION_ID='+STID+'&WATERLEVEL_6MIN_VFD_PX._DATUM='+DATUM+'&WATERLEVEL_6MIN_VFD_PX._BEGIN_DATE='+T1+'&WATERLEVEL_6MIN_VFD_PX._END_DATE='+T2
    f=requests.get(URL)
    s=f.text
    s=s.split('\n')
    HDREND = u'---------------------------------------------'
    ihe=s.index(HDREND)
    #VARS   = u'WATERLEVEL_6MIN_VFD_PX.DATE_TIME, WATERLEVEL_6MIN_VFD_PX.WL_VALUE'
    VARS=s[ihe+1]
    s=s[ihe+2:]

    for i in range(len(s)):
        try:
	    [T,H]=s[i].split(',')
#T=u'"Mar  1 2014 12:18AM"'
#H=u' 1.457'
	    t=np.append(t,datetime.strptime(T.strip('"'),'%b %d %Y %I:%M%p'))
	    h=np.append(h,float(H))
        except:
# last line is empty
	    pass

# output numpy arrays
# t - time, python datetime UTC
# h - water level, m

plt.figure()
plt.plot(t,h,'b-')
plt.show()


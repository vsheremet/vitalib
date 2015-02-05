import numpy as np

import datetime
t=datetime.datetime.strptime('2014-09-10 11:08:15.21','%Y-%m-%d %H:%M:%S.%f') 

# smart date time parser
import dateutil.parser                                                
S1='2013-04-21T15:14:159265Z'                                        
t1=dateutil.parser.parse(S1)                                           
S2='04/21/2013 15:14'                                        
t2=dateutil.parser.parse(S2)      

a=np.array([11.,12.,13.,14.,15.])
for idx, val in enumerate(a):
    print(idx,val)
    
#    if __name__ == "__main__":

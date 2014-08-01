import numpy as np
from datetime import datetime

def sh_fun(req_arg, *args, **kwargs):
    """
    sh_fun - function template
    
    sh_fun(req_arg, *args, **kwargs)
    
    ver 2.0.1 2014-08-01
    """
    
    print 'sh_fun(',req_arg,',',args,',',kwargs,')'
    FN=req_arg
    
    if len(args)==1:
        FN1=args[0]
        print FN1
        
    if len(args)==2:
        FN2=args[1]
        print FN2
    
        

    T1=kwargs.get('T1','0001-01-01 00:00:00')
    T2=kwargs.get('T2','9999-12-31 23:59:59')

    if 'T1' in kwargs:
        T1=kwargs['T1']
    else:
        T1='0001-01-01 00:00:00'
        
    if 'T2' in kwargs:
        T2=kwargs['T2']
    else:
        T2='9999-12-31 23:59:59'
        

    print FN
    print T1
    print T2
    
#

sh_fun('123.txt')
sh_fun('123.txt',T1='2004',T2='2005')
sh_fun('123.txt','456.txt',T1='2004',T2='2005')
sh_fun('123.txt','456.txt','456.dat',MAvg=5)


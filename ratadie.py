def RataDie(yr,mo=1,da=1,hr=0,mi=0,se=0):
    """

RD = RataDie(yr,mo=1,da=1,hr=0,mi=0,se=0)    

returns the serial day number in the (proleptic) Gregorian calendar
or elapsed time in days since 0001-01-00.

The Gregorian calendar starts with January 1, year 1, as day 1 (Monday).
It has a 400 year cycle (of which 97 are leap years) of 146097 days, 
20871 seven-day weeks. 
RataDie(1,1,1) -> 1  (Monday)
RataDie(2001,1,1) -> 146097*5+1 = 730486 (Monday)

RataDie is same as Python date2num or toordinal.
MATLAB datenum has January 1, year 0 as day 1, therefore
MATLAB datenum = RataDie + 366

mo,da,hr,mi,se may be outside valid calendar ranges, e.g.,
2001,1,121 is the yearday 121 of 2001;
2001,1,0 is 2000-12-31;
2001,-1,21 is 2000-11-21
2001,1,1,25 is 2001-01-02 01:00:00

da,hr,mi,se may have fractional parts.

The extension of the argument ranges is the primary goal of introducing 
this function as the python datetime would reject such arguments.

If TIMESTAMP='2001-01-121' is a string, use 
(YYYY,MM,DD)=TIMESTAMP.split('-')
yr,mo,da=int(YYYY),int(MM),float(DD)
or
yr,mo,da,hr,mi,se=sh_parse_timestamp(TIMESTAMP)

Vitalii Sheremet, SeaHorse Project, 2008-2013.
    """
#
    yr+=(mo-1)//12;mo=(mo-1)%12+1; # this extends mo values beyond the formal range 1-12
    RD=367*yr-(7*(yr+((mo+9)//12))//4)-(3*(((yr+(mo-9)//7)//100)+1)//4)+(275*mo//9)+da-396+(hr*3600+mi*60+se)/86400.;
    return RD

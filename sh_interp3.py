def sh_interp3(ti,t,f):
    """
    interpolates irragularly spaced 1D data to uniform grid
    using cubuc Hermite spline.
    http://en.wikipedia.org/wiki/Cubic_Hermite_spline
    tangents are defined as a finite difference approximation of derivative
    interpolation formula is expressed in terms of 
    Bernstein polynomials of 3rd order: B_0,B_1,B_2,B_3.

    Vitalii Sheremet, SeaHorse Project
    """
    m=f*0. # derivative
    N=len(f)
    for i in range(1,N-1):
# In this version the tangent m is a plain average of differences from two sides
# which is not consistent with the finite difference
# approximation of a derivative on a nonuniform grid
#        m[i]=((f[i+1]-f[i])/(t[i+1]-t[i])+(f[i]-f[i-1])/(t[i]-t[i-1]))*0.5
# This version of the tangent m is the finite difference
# approximation of a derivative on a nonuniform grid 
        ha=t[i+1]-t[i]
        hb=t[i]-t[i-1]        
        m[i]=((f[i+1]-f[i])*hb/ha+(f[i]-f[i-1])*ha/hb)/(ha+hb)
    # ends
    m[0]  =2.*(f[1]  -f[0])  /(t[1]  -t[0])  -m[1]
    m[N-1]=2.*(f[N-1]-f[N-2])/(t[N-1]-t[N-2])-m[N-2]    
        
    # 
    fi=ti*0.
    NN=len(ti)
    for ii in range(NN):
        i=max(np.argwhere(t<=ti[ii])) # left end of segment
        dt=t[i+1]-t[i]
        a=(ti[ii]-t[i])/dt  # 0<a<1 normalized coordinate within a segment 
        b=1.-a
        # multiply f and m*dt must have the same dimensions
        fi[ii]=(b*b*b+3.*a*b*b)*f[i]+(a*a*a+3.*b*a*a)*f[i+1]+(a*b*b*m[i]-b*a*a*m[i+1])*dt
    
    return fi

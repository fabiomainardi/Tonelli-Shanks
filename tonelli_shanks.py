# Tonelli-Shanks algorithm
# p is prime
# solves the congruence x^2 = n mod p
def TS(p,n):
    import math
    if(int(math.pow(n,(p-1)/2))%p !=1):
        return("No solutions")
    # find max power of 2 dividing p-1
    s=0
    while((p-1)%math.pow(2,s)==0):
        s+=1
    s-=1
    q=int((p-1)/math.pow(2,s))# p-1=q*2^s
    # Select a z such that z is a quadratic non-residue modulo p
    z=1
    res=int(math.pow(z,(p-1)/2))%p
    while(res !=p-1):
        z+=1
        res=math.pow(z,(p-1)/2)%p
    c=int(math.pow(z,q))%p
    r=int(math.pow(n,(q+1)/2))%p
    t=int(math.pow(n,q))%p
    m=s
    while(t%p !=1):
        i=0
        div=False
        while(div==False):
            i+=1
            t=int(math.pow(t,2))%p
            if(t%p==1):
                div=True
        b=int(math.pow(c,int(math.pow(2,m-i-1))))%p
        r=(r*b)%p
        t=t*(b**2)%p
        c=(b**2)%p
        m=i
        
    return r
    
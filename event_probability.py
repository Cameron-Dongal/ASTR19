import sys
import numpy as np
from scipy.special import erf

def event_probability(x,mu=0.0,s=1.0):
    #x is val of event
    #mu si gaussian mean
    #s is gaussian stddev
    z=np.fabs((x-mu)/s)
    def zfunc(z):
        return 0.5*(1.0+erf(z/2**.5))
    
    #return prob of getting event of magnitude >= x
    return 1.0-(zfunc(z)- zfunc(-1*z))
def main():
    x=3.
    if (len(sys.argv)>1):
        x=float(sys.argv[1])

    prob=event_probability(x)
    print(f"The gaussian probability of events larger than |{x}| is {prob*100:6.4f}%.")
    print(f"The Gaussian probability of events smaller than |{x}| is {(1-prob)*100:6.4f}%.")


if __name__=="__main__":
    main()
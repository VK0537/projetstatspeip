from statslib import Stat
from random import randint
# import numpy as np
import statistics
from math import pi, sqrt, exp

# def h(x):return abs((1/2)*(exp(x)+exp(-x))*sin(x))
z=[130,140,170,160,136,165,130,135,140,135,161,136,180,190,141,132,165,168,182,177,172,168,175,181,173,169,178,179,175,164]
# z=[130,140,170,160,136,165,130,135,140,135,161,136,180,190,141,132,165,168,182,177,172,168,175,181,173,169,178,179,175]
# def k(x):return (x**3+3*x**2 if x<=0 else (x**(-1) if x<4 else x**2-7/2*x))
def gauss(x,u=0,o=1): return exp(-((x-u)**2)/abs(2*o**2))/abs(sqrt(2*pi)*o)
ex=Stat(z)
# ex=Stat(gauss,-10,10,0.1)
# print(ex)
# print(ex.serie)
# print(ex.quan(4))
# print(statistics.quantiles(z))
# print(sorted(z))

# print(ex.ecartmoy())
# print(ex.variance())
# print(ex.ecarttyp())
# print(ex.med())
print(ex.mmt(1),ex.moy())
print(ex.mmtctr(2),ex.variance())
# print(ex.mmt(2))
# print(ex.mmtctr(2))
# print(ex.mmt(0),ex.mmtctr(0))
# print(ex.mmtctr(1))
# print(ex.mmt(1),ex.moy())
# print(ex.mmtctr(2),ex.variance(),ex.mmt(2)-ex.mmt(1)**2)
# print(ex.asym(),ex.apla())

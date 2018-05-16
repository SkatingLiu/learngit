'''
Algorithm : SLiMFsat's optimizer
input : objects O, source observations Q, source features K, Ground truth G, threshold t
output : learning Algorithm ( ERM is 0, EM is 1)
'''
import math

def optimizer(units):
    Q = []
    G = []
    K = []
    t = 0.01
    if math.sqrt(len(K)/len(G))*math.log(len(G)) < t :
        return 0
    ERMunits = len(G)
    EMunits = units
    if ERMunits < EMunits :
        return 1
    else:
        return 0

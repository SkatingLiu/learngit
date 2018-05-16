'''
Algorithm : Estimating information units for EM
Input : source observation , object , average source accuracy A
Output : EM information units

m = # of sources with observations for o
D0 = # of distinct values assigned to o by sources
'''

import math
import numpy as np

def EMunits(A):
    # calculate the number of source observation
    Q = []
    observation = []
    q_number = len(Q)
    for i in range(0, q_number):
        observation.append(Q[i][1])
    observation_set = set(observation)
    o_number = len(observation_set)
    # calculate units
    D0 = 2
    O = []
    units = 0
    for i in range(0,o_number):
        m = len(O[i])
        n = math.floor(m/D0)
        n = math.int(n)
        pe = 1 - np.random.binomial(n, A, size=None)
        if pe >= 0.5 :
            units +=  1 - pe * math.log(pe,2) - (1 - pe) * math.log(1-pe,2)

    return units
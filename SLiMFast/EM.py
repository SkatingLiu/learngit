'''
aim : use EM to calculate source accuracy
input : observation Q , feature K
output : w and source realibility
 
'''
import math

def EM():
    # imagine Q and G has the same number objects
    Q = []
    Q1 = []
    Ht = []  # object value
    Hf = []
    source = [] # the number of source , per source has the number of object
    # w = n * (k+1)
    w = []  # importance of feature
    w1 = []
    F = []  # feature matrix
    nums = len(Q)
    t = [] # threshold
    ht = 0 , hf = 0
    while True :
        for i in range(nums):
            source_num = len(Q1[i])
            for j in range(source_num):
                if Q[i][2]==True :
                    ht += w[j]*F[i]
                else :
                    hf += w[j]*F[i]
            # accuracy of object's value
            Ht[i] = math.exp(ht) / ( math.exp(ht) + math.exp(hf))
            Hf[i] = 1 - Ht[i]
        # E-step
        for i in range(nums):
            source_num = len(Q1[i])
            for j in range(source_num):
                if Q[i][2]==True :
                    ht += w[i]*F[i]
                else :
                    hf += w[i]*F[i]
            Q += Ht[i] * ht + Hf[i] * hf
        # M-step
        # per source has the number of object
        for i in range(source):
            object_num = len(source[i])
            for j in range(object_num):
                if Q[i][2]==True :
                    w1[i] += F[i] * Ht[j]
                else :
                    w1[i] += F[i] * Hf[j]
        # w1[i] is the max likelihood
        for i in range(source):
            T += math.fabs(w[i] - w1[i])
            w[i] = w1[i]
            if T < t :
                return w
'''
aim : use ERM to calculate source accuracy
input : observation Q , feature K , ground truth G
output : w and source realibility
'''

import math
import numpy as np

def ERM():
    # imagine Q and G has the same number objects
    Q = [],Q1 = []
    G = [] # ground truth
    H = [] # object value
    # w = n * (k+1)
    w = [] # importance of feature
    F = [] # feature matrix
    nums = len(G)
    cnt = 0 # records of iteration
    L1 = 100 # loss function
    L = 0
    a = [0.1 , 0.3 , 0.5]
    while cnt<1000:
        cnt = cnt + 1
        for i in range(nums):
            source_num = len(Q1[i])
            for j in range(source_num):
                if Q[i][2]==True :
                    ht += w[i]*F[i]
                else :
                    hf += w[i]*F[i]
            # judge object's value
            if ht > hf :
                object = True
            else :
                object = False
            H[i] = object
            # judge object and truth , if true ,loss function plus 0; else plus 1
            if G[i][1] == object :
                L += 0
            else :
                L += 1
        if math.fabs(L1 - L) < 10:
            return w
        else :
            L1 = L

        # update w
        for i in range(n):
            w[i] = w[i] + a * (G[i][1]-H[i]) * F[i]
'''
Q source obversation list
\S\ the number of data sources

'''
import math
import numpy as np


def Accuracy():
    # calculate the number of data sources
    Q = []
    list_source = []
    q_number = len(Q)
    for i in range(0,q_number):
        list_source.append(Q[i][0])
    list_source_set = set(list_source)
    S_number = len (list_source_set)
    # calculate agreement rate X
    S  = []
    X = []
    for i in range(0,S_number):
        for j in range(0,S_number):
            if i==j:
                continue
            Os,ij = [i for i in S[i] if i in S[j]]
            Os, ij_number = len (Os,ij)
            for k in range(0,Os,ij_number):
                if S[i][k]==S[j][k]:
                    X[i][j] += 1/Os,ij_number
            X += X[i][j]
    # calculate A
    u = np.sqrt(X/(math.pow(S_number,2)-S_number))
    A = (u+1)/2
    return A

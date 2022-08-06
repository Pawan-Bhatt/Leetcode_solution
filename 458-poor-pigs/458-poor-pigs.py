class Solution:
    def poorPigs(self, B, D, T):
	    tmp = log2(B) # number of pigs for one shot
	    t = ceil(T/D) # number of tests we can conduct

	    if t == 1: return ceil(tmp) # one shot is the answer
	    return ceil(tmp / log2(t+1)) # re-use pigs until the answer is found (# of tests)
        
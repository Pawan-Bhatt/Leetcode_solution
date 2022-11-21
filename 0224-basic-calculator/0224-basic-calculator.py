class Solution:
    def calculate(self, ss: str) -> int:
        
        stack, acc, n, s = [], 0, 0, +1                   # stack, running sum, number & sign
        
        for c in ss:
            
            if c.isdigit() : n = 10*n + int(c)            # accumulate number from digits
            
            if c in "+-": 
                acc += s*n                                # update sum with last sign and number
                n, s = 0, (c=="+")*2 - 1                  # start new number and set new sign
            
            if c == "(":
                stack += (acc, s)                         # push accumulated sum and last sign to stack
                acc, s = 0, +1                            # and initialize them for the use inside (...)
            
            if c == ")":
                acc += s*n                                # add last number to the result in (...)
                acc = acc * stack.pop() + stack.pop()     # join results in (...) with previous result
                n, s = 0, +1                              # start new number
        
        return acc + s*n                                  # in the end, we may have one number left
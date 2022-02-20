def getSum(n):
        summ = 0
        for digit in str(n): 
            summ += int(digit)      
        return summ
class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        temp = 2
        while temp <= num:
            if getSum(temp) %2 == 0:
                count+=1
            temp+=1
        return count
        
        
    
    
        
        

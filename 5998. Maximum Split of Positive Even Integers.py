class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        arr = [] 
        summ = 2
        if finalSum % 2 ==0:
            while finalSum > 0:
                finalSum -= summ
                arr.append(summ)
                summ += 2
            if -finalSum in arr:
                arr.remove(-finalSum)
        return arr
                
                
                
                

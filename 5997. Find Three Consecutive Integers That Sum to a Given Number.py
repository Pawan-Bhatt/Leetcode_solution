class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        arr = []
        x = (num-3) // 3
        if (3*x +3) == num:
            arr.append(x)
            arr.append(x+1)
            arr.append(x+2)
        return arr
        
        

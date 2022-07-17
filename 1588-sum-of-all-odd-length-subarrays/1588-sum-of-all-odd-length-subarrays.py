class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        count = 0    
        n = len(arr)
    
        for i in range(n):
            start = (n - i)
		
		# How many subarrays end at index, i
            end = i + 1
		
		# Total number of subarrays
            total = start * end
		
		# Get odd subarrays
            odd = total // 2
        
            if total % 2 == 1:
                odd += 1
        
		# Increment the sum of odd length subarrays
            count += odd * arr[i]
            print(start, end, total, odd, count)
        
        return count
        
#User function Template for python3
import math
class Solution:
    def rec_(self, nums, N, K, index, mem):
        if index == N - 1:
            return 0
        if mem[index] != -1:
            return mem[index]
        _sum = 0
        _cost = math.inf
        for i in range(index, N):
            _sum += nums[i]
            if (_sum + i-index) <= K:
                if i == N-1:
                    _cost = 0
                    break
                spaces = K - (_sum + i-index)
                _cost = min(_cost, spaces**2 + self.rec_(nums, N, K, i+1, mem))
            else:
                break
        mem[index] = _cost
        return mem[index]

    def solveWordWrap(self, nums, K):
        N =len(nums)
        mem = [-1]*N
        return self.rec_(nums, N, K, 0, mem)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		k = int(input())
		obj = Solution()
		ans = obj.solveWordWrap(nums, k)
		print(ans)


# } Driver Code Ends
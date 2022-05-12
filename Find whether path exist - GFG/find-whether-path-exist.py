

class Solution:	
    def is_Possible(self, grid):
		stx = 0
		sty = 0
		n = len(grid)
		for i in range(n):
		    for j in range(n):
		        if grid[i][j] == 1:
		            stx = i
		            sty = j
		            break
	    def solve(x,y):
	        if x<0 or x>=n or y<0 or y>=n or grid[x][y]==0 or grid[x][y] ==-1:
	            return False
	        if grid[x][y] == 2:
	            return True
	        grid[x][y] = -1
	        return solve(x+1,y) or solve(x-1,y) or solve(x,y+1) or solve(x,y-1)
	    return solve(stx,sty)

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.is_Possible(grid)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
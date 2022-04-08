from collections import Counter
class Solution:
    def print_next_greater_freq(self,arr,n):
        c = Counter(arr)
     
        idx = [-1]*n
        
        stack = []
        for i, v in enumerate(arr):
            if not stack:
                stack.append(i)
            else:
                cur_freq = c[v]
                while stack:
                    last_idx = stack[-1]
                    last_freq = c[arr[last_idx]]
                    if last_freq < cur_freq:
                        idx[last_idx] = v
                        stack = stack[:len(stack)-1]
                    else:
                        break
                stack.append(i)
                
        return idx

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        obj=Solution()
        ans=obj.print_next_greater_freq(arr,n)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends
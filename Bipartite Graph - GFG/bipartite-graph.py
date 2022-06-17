class Solution:
	def isBipartite(self, V, adj):
		vis=[False]*V
		color=[False]*V
		q=[]
		i=0
		while i<V:
		    if vis[i]==True:
		        i+=1
		        continue
		    q.append(i)
		    vis[i]=True
		    color[i]=True
		    while len(q)>0:
		        ele=q.pop(0)
		        for neb in adj[ele]:
		            if not vis[neb]:
		                q.append(neb)
		                vis[neb]=True
		                color[neb]= not color[ele]
		            elif color[neb]==color[ele]:
		                return False
		    i+=1
		return True

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
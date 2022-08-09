class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 1000000007
        dic = {num: 1 for num in arr}
        arr.sort()

        for i in range(1, n):
            for j in range(i):
                quot = arr[i] // arr[j]
                if quot < 2:
                    break
                if arr[i] % arr[j] == 0 and quot in dic:
                    dic[arr[i]] += dic[arr[j]] * dic[quot]
                    dic[arr[i]] %= mod
        print(dic)
        return sum(dic.values()) % mod
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr=nums
        self.n=k

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr)-self.n]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
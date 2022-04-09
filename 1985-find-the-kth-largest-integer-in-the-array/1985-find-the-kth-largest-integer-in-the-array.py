class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        results = list(map(int, nums))
        results.sort()
        return str(results[-k])
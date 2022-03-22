class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        counter = 1
        if n % 2 == 1:
            arr.append(0)
            n -= 1
        times = n // 2
        for i in range(times):
            arr.append(-1 * counter)
            arr.append(counter)
            counter += 1
        return arr
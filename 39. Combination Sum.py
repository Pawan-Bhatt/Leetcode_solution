class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []                                   # for adding all the answers
        def traverse(candid, arr,sm):                   # arr : an array that contains the accused combination; sm : is the sum of all elements of arr 
            if sm == target: self.ans.append(arr)       # If sum is equal to target then you know it, I know it, what to do
            if sm >= target: return                     # If sum is greater than target then no need to move further.
            for i in range(len(candid)):                # we will traverse each element from the array.
                traverse(candid[i:], arr + [candid[i]], sm+candid[i])   #most important, splice the array including the current index, splicing in order to handle the duplicates.
        traverse(candidates,[], 0)
        return self.ans

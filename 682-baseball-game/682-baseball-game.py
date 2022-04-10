class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ary = []
        for i in range(len(ops)):
            if ops[i]=="C":
                ary.pop()
            elif ops[i]=="D":
                ary.append(ary[-1]*2)
            elif ops[i]=="+":
                ary.append(ary[-1]+ary[-2])
            else:
                ary.append(int(ops[i]))
        return sum(ary)
    
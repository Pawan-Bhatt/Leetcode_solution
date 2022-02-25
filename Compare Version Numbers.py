class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split('.')
        b = version2.split('.')
        a=[int(i) for i in a]
        b = [int(i) for i in b]
        i=0
        j=0
        while i<len(a) or j<len(b):
            x=0
            y=0
            if j<len(b):
                y=b[j]
            if i<len(a):
                x=a[i]
            if x==y:
                i+=1
                j+=1
            elif x>y:
                return 1
            elif x<y:
                return -1
        return 0

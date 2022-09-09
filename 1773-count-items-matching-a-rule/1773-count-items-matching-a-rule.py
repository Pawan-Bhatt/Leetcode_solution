class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        if ruleKey == "type":
            num = 0
        elif ruleKey == "color":
            num = 1
        else:
            num = 2
        for item in items:
            if(item[num] == ruleValue):
                count+=1
        return count
            
            
        
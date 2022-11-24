class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Row, Col, and subBox will each contain 9 sets to keep track of the visited element.
        # Using 0-8 as the id for each row, col, and sub-box.
        # At any time if the same number is visited twice, return False. 
        Row = defaultdict(set)
        Col = defaultdict(set)
        subBox = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                
                cur = board[r][c]
                if cur=='.':
                    continue
                
                # r is the id for Row 
                if cur in Row[r]:
                    return False
                Row[r].add(cur)
                
                # c is the id for Col
                if cur in Col[c]:
                    return False
                Col[c].add(cur)
                
                # sub-box id is a little bit tricky
                # r//3*3 will map the number 0-8 to 0,3,6 which is the starting id for each row.
                # c//3 will map the number 0-8 to 0,1,2, which is the column.
                # So r//3*3+c//3 is corresponding to sub-box id as shown
                                                             
                boxId = r//3*3+c//3                        
                if cur in subBox[boxId]:                   
                    return False                          
                subBox[boxId].add(cur)                    
                                                          
        # We passed all the tests, return True
        return True
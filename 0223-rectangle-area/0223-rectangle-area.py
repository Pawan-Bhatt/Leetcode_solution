class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def area(x1,y1,x2,y2):
            return (x2-x1)*(y2-y1)
        xOverlap = max(min(ax2,bx2)-max(ax1,bx1), 0)
        yOverlap = max(min(ay2,by2)-max(ay1,by1), 0)
        return area(ax1,ay1,ax2,ay2) + area(bx1,by1,bx2,by2) - xOverlap*yOverlap
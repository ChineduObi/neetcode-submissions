class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        joined = []
        

        for i in matrix:
            joined += i
        
        print(joined)

        l, r = 0, len(joined) - 1
        while l <= r:
            mid = (l + r)//2

            if joined[mid] == target:
                return True
            elif joined[mid] < target:
                l = mid +1
            else:
                r = mid - 1

        return False
            

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]== target:
                    return True
        return False
    
#Brute force solution with O(m*n) time complexity
        
 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        i, j = 0, n-1
        
        while i<m and j >=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -=1
            else:
                i +=1
        
        return False
    
# Pointer solution with O(m+n) time complexity
# Space complexity is O(1)
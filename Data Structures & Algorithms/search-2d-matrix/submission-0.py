class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        LOW , HIGH = 0 , len(matrix) -1

        while HIGH >= LOW:
            MID = (HIGH + LOW) // 2

            low , high = 0 , len(matrix[MID]) - 1

            while high >= low:
                mid = (high + low) // 2
                if matrix[MID][mid] > target:
                    high = mid - 1
                elif matrix[MID][mid] < target:
                    low = mid + 1
                else:
                    return True

            if matrix[MID][-1] > target:
                HIGH = MID - 1
            elif matrix[MID][-1] < target:
                LOW = MID + 1
            else:
                return True
        return False
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        spiral = []
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while top <= bottom and left <= right:
            # Traverse top from left to right
            for column in range(left, right + 1):
                spiral.append(matrix[top][column])
            top += 1

            # Traverse top to bottom along right column
            for row in range(top, bottom + 1):
                spiral.append(matrix[row][right])
            right -= 1

            # Traverse bottom from right to left
            if top <= bottom:
                for column in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][column])
                bottom -= 1

            if left <= right:
                # Traverse bottom to top along left column
                for row in range(bottom, top - 1, -1):
                    spiral.append(matrix[row][left])
                left += 1

        return spiral

        

        
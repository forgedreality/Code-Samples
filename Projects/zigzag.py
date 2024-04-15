# zigzag conversion
# https://leetcode.com/problems/zigzag-conversion/
# ***INCOMPLETE***
class Solution:
    def getSubs(self, arr, s, e, subs=[]):
        if e == len(arr):
            return
        elif s > e:
            return getSubs(arr, 0, e + 1)
        subs.append(arr[s:e+1])
        return getSubs(arr, s + 1, e)


    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1 or numRows > len(s): return s

        out = [None] * numRows
        curr_row = 0
 
        for char in s:
            if curr_row == 0:
                down = True
            if curr_row == numRows - 1:
                down = False

            out[curr_row] = char if out[curr_row] == None else out[curr_row] + char

            curr_row += 1 if down else -1

        return ''.join(out)

a = Solution()
print(a.convert('PAYPALISHIRING', 3))

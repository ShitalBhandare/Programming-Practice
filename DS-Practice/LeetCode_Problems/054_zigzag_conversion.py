
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only one row, return original string
        if numRows == 1:
            return s
      
        # Initialize a list of empty lists, one for each row
        rows = [[] for _ in range(numRows)]
      
        # current_row: tracks which row we're currently adding to
        # direction: determines if we're moving down (1) or up (-1) in the zigzag
        current_row = 0
        direction = -1
      
        # Iterate through each character in the string
        for char in s:
            # Add current character to the appropriate row
            rows[current_row].append(char)
          
            # Change direction when we reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                direction = -direction
          
            # Move to the next row based on current direction
            current_row += direction
      
        # Concatenate all rows together to form the final string
        # Using list comprehension to join each row, then join all rows
        return ''.join(''.join(row) for row in rows)

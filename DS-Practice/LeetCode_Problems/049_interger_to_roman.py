'''
Problem Description
You need to convert an integer into its Roman numeral representation.

Roman numerals use seven different symbols with specific values:

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
The conversion follows these rules:

Basic Rule: Build the Roman numeral by converting decimal place values from highest to lowest. For most values, repeatedly use the largest possible symbol that doesn't exceed the remaining number.

Subtractive Form: When a decimal place value starts with 4 or 9, use a special subtractive notation:

4 → IV (1 before 5)
9 → IX (1 before 10)
40 → XL (10 before 50)
90 → XC (10 before 100)
400 → CD (100 before 500)
900 → CM (100 before 1000)
Repetition Limits: Powers of 10 (I, X, C, M) can appear at most 3 times consecutively. The symbols V, L, and D cannot be repeated. If you would need 4 of the same symbol, use the subtractive form instead.

'''

class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert an integer to Roman numeral representation.
      
        Args:
            num: Integer to convert (1 <= num <= 3999)
          
        Returns:
            String representation of the Roman numeral
        """
        # Define Roman numeral symbols and their corresponding values
        # Ordered from largest to smallest, including subtractive notation cases
        roman_symbols = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        decimal_values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
      
        # List to collect Roman numeral parts
        result = []
      
        # Iterate through each Roman symbol and its value
        for symbol, value in zip(roman_symbols, decimal_values):
            # Greedily subtract the largest possible value
            while num >= value:
                num -= value
                result.append(symbol)
      
        # Join all parts into final Roman numeral string
        return ''.join(result)

'''
Run length encoding program. 
For example, if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6”
'''

def run_length_encoding(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    
    encoded = []
    count = 1
    
    for i in range(1, n):
        if s[i] == s[i-1]:
            count += 1
        else:
            encoded.append(f"{s[i-1]}{count}")
            count = 1
    
    encoded.append(f"{s[-1]}{count}")
    return "".join(encoded)

# Example usage
input_string = "wwwwaaadexxxxxx"
encoded_string = run_length_encoding(input_string)
print(encoded_string)  # Output: "w4a3d1e1x6"


===================


'''
Other way of using OrderedDict

'''

# Run Length Encoding of a string
def run_length_encoding_string(s):
    d = OrderedDict()
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return ''.join(f"{char}{count}" for char, count in d.items())

# Example usage
s = "wwwwaaadexxxxxx"
encoded_string = run_length_encoding_string(s)
print("Encoded String:", encoded_string)

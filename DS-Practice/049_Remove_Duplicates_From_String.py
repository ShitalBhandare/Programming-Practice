# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

from collections import OrderedDict


'''
def remove_duplicates(input_string):
    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

# Example usage
input_string = "AaBbCcAa"
output_string = remove_duplicates(input_string)
print(f"Original string: {input_string}")
print(f"String after removing duplicates: {output_string}")

****************************************************

def remove_duplicates(s):
    seen = set()
    s = list(s)
    write_index = 0
    for read_index in range(len(s)):
        if s[read_index] not in seen:
            seen.add(s[read_index])
            s[write_index] = s[read_index]
            write_index += 1
    return ''.join(s[:write_index])

# Example usage
input_string = "geEksforGEeks"
output_string = remove_duplicates(input_string)
print(f"Original string: {input_string}")
print(f"String after removing duplicates: {output_string}")
'''

def remove_duplicates(s):
    return ''.join(OrderedDict.fromkeys(s))

# Example usage
input_string = "geEksforGEeks"
output_string = remove_duplicates(input_string)
print(f"Original string: {input_string}")
print(f"String after removing duplicates: {output_string}")

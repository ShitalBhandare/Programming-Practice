'''
Program to print last 10 lines fo big string or big file
'''

def print_last_10_lines(big_string):
    lines = big_string.split('\n')
    last_10_lines = lines[-10:]
    for line in last_10_lines:
        print(line)

# Example usage
big_string = """Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Line 11
Line 12
Line 13
Line 14
Line 15"""

print_last_10_lines(big_string)
def print_last_10_lines_of_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_10_lines = lines[-10:]
        for line in last_10_lines:
            print(line, end='')

# Example usage
file_path = 'path_to_your_file.txt'
print_last_10_lines_of_file(file_path)

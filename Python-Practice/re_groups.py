
# Hello World program in Python
    
import re
string = "2017@12249"
match = re.search(r'([\d]+)@([\d]+)', string)

#match = re.search(r'([\w.-]+)@([\w.-]+)', str)

if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2).split())


str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    print(match.group())  ## 'alice-b@google.com' (the whole match)
    print(match.group(1))  ## 'alice-b' (the username, group 1)
    print(match.group(2))  ## 'google.com' (the host, group 2)
	

Output:

$python3 main.py
2017@12249
2017
['12249']
alice-b@google.com
alice-b
google.com
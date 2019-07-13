
# Hello World program in Python
    
import re

string = "I want to go USA. I want to buy car"
match = re.search("USA", string)
print(match.group())

match1 = re.match("I", string)
print(match1.group())

print(re.sub("want", "desire", string))




output:

$python3 main.py
USA
I
I desire to go USA. I desire to buy car
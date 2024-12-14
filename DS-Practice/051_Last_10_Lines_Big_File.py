'''
Given some text lines in one string, each line is separated by ‘\n’ character. 
Print the last ten lines. If number of lines is less than 10, then print all lines.
'''

str1 = "a\nb\nc\nd\ne\nf\ng\nh\nk\nl\nm\nn\no\np\nq\nr\ns\nt"
#str1 = "a\nb\nc"
#str1 = ""

l1 = str1.split("\n")
print(l1)
print("\n".join(l1[-10:]))


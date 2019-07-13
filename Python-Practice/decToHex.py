

'''



def covertTohex(decimal):
  base = 16
  a_dict = {'A':}
  quotient = decimal // base
  
  remainder = []
  remainder.append(str(decimal % base))
  while (quotient != 0):
    remainder.append(str(quotient % base))
    quotient = quotient // base
    remainder.append(str(quotient % base))
  
  #print(remainder)
  print("".join(remainder[::-1]))


if __name__ == "__main__":
  decimal = input("Enter decimal no:")
  covertTohex(int(decimal))
'''


h=[str(i) for i in range(10)]+["A","B","C","D","E","F"]
def hexa(dec):
  s=""
  while dec:
    s+=h[dec%16]
    dec//=16
  print(s[::-1])

hexa(40)


Output=>

Python 3.6.1 (default, Dec 2015, 13:05:11)
[GCC 4.8.2] on linux
28

# Driver Code 
'''
IPv4 address validation
'''
import re


regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][-0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][-0-9]|[1-9]?[0-9])$"


def check(ip):
    
    if (re.search(regex, ip)):
        print("Valid")
    else:
        print("Invalid")

if __name__ == '__main__' : 
    
    # Enter the Ip address
    Ip = "192.168.0.1"
    
    # calling run function 
    check(Ip)

    Ip = "110.234.52.124"
    check(Ip)

    Ip = "366.1.2.2"
    check(Ip)

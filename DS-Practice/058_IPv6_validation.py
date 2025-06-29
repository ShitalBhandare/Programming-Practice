# Driver Code 
'''
IPv6 address validation
The regex to validate ipv6 is huge and not readable. 
Hence, doing it via code
'''


def isValid(ip):
    
    if not ip:
        return False
    
    #if len(ip) < 15:
    #    return False
    
    ipv6_parts = ip.split(":")
    
    if len(ipv6_parts) != 8:
        return False
    
    for part in ipv6_parts:
        if len(part) > 4 or len(part) == 0:
            return False
            
        for char in part:
            if not (char.isdigit() or  'a' <= char <= 'f' or  'A' <= char <= 'f'):
                return False
                
    return True
    

# Test cases
ip1 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
ip2 = "fe80::1"
ip3 = "2001:db8:85a3::8a2e:370:7334"
ip4 = "2001:0db8:85a3:xyz:0000:8a2e:0370:7334"

print(f"{'Valid' if isValid(ip1) else 'Not valid'}")
print(f"{'Valid' if isValid(ip2) else 'Not valid'}")
print(f"{'Valid' if isValid(ip3) else 'Not valid'}")
print(f"{'Valid' if isValid(ip4) else 'Not valid'}")

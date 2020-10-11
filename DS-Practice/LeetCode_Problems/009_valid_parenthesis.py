'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        '''
        if not s:
            return True
        
        stack = []
        
        for paren in s:
            if paren in ['(', '{', '[']:
                stack.append(paren)
            else:
                if stack:
                    p = stack.pop()
                else:
                    return False
                if (paren == ')' and p == '(') or (paren == ']' and p == '[') or (paren == '}' and p == '{'):
                        continue
                else:
                    return False
                
        return True if not stack else False
                
        '''
        if not s:
            return True
        
        stack = []   
        hash_map = {")":"(", "]":"[", "}":"{"}
        for paren in s:
            if paren in hash_map:
                if stack:
                    top = stack.pop()
                else:
                    return False
                if top != hash_map[paren]:
                        return False
            else:
                stack.append(paren)
                       
        return True if not stack else False
                
                    
'''
Time Complexity: O(n)
Space Complexity: O(n)
'''

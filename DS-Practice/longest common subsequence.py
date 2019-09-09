
'''
Longest Common Subsequence Problem
str1 = "ABCDGH" 
str2 = "AEDFHR"
Longest Common Subsequence: "ADH" of length 3
'''

def findLongComm_Subseq(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    matrix = [[0 for j in range(len2 + 1)] for i in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
            
            
    return matrix[len1][len2]
            
if __name__ == "__main__":
    #str1 = "AGGTAB"
    #str2 = "GXTXAYB"
    
    str1 = "ABCDGH" 
    str2 = "AEDFHR"
    
    result = findLongComm_Subseq(str1, str2)
    print("The longest common subsequence:", result)

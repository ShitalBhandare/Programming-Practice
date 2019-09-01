# Program to find length of longest common substring in Python

def find_longest_com_str(str1, str2, len1, len2):
    
    matrix = [[0 for j in range(len2+1)] for i in range(len1+1)]
    
    result = 0
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
                result = max(result, matrix[i][j])
            else:
                matrix[i][j] = 0
    
    return result
    


if __name__ == "__main__":
    
    str1 = "GeewrksforGete4eks"
    str2 = "GeeksQuiz"
    
    len1 = len(str1)
    len2 = len(str2)
    
    result = find_longest_com_str(str1, str2, len1, len2)
    print("Longest common substring is of length", result)
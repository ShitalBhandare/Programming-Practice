

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''
Egg Dropping problem using Dynamic Programming
'''

INT_MAX = 32767

def eggdrop(n, k):
    
    result = [[0 for x in range(k+1)] for x in range(n+1)]
    
    for i in range(n+1):
        result[i][0] = 0
        result[i][1] = 1 
    
    for j in range(k+1):
        result[1][j] = j
        
    for i in range(2, n+1):
        for j in range(2, k+1):
            result[i][j] = INT_MAX
            for x in range(1, j+1):
                res = 1 + max(result[i-1][x-1], result[i][j-x])
                if res < result[i][j]:
                    result[i][j] = res
                
    return result[n][k]

if __name__ == "__main__":
    n = 2
    k = 36
    min_try = eggdrop(n, k)
    print("The minimum try with", n, "eggs and", k, " floors :", min_try)


# Coin change problem

'''
We have infinite supply of coins.
coins = [1, 2, 3]
sum = 4
We need to find different ways using which we can achieve the given sum.
No. of ways = 4 
[1,1,1,1], [1,1,2], [2,2], [1,3]
'''

def find_coin_change(coins, n, sum):
    
    matrix = [[0 for j in range(sum+1)] for i in range(n+1)]

    for i in range(n+1):
        matrix[i][0] = 1
        
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j < coins[i-1]:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-coins[i-1]]
                
    return matrix[n][sum]

if __name__ == "__main__":
    coins = [1, 2, 3]
    sum = 4
    n = len(coins)
    
    result = find_coin_change(coins, n, sum)
    print("No. of ways we achieve the sum using coins: ", result)


=============================
'''
We have infinite supply of coins.
coins = [1, 2, 3]
sum = 4
We need to find minimum number of coins using which we can achieve the given sum.
Minimum no of coins = 2
[3, 1]
'''

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def find_coin_change(coins, n, sum):
    
    matrix = [[0 for j in range(sum+1)] for i in range(n+1)]

    for j in range(sum+1):
        matrix[0][j] = j
        
    print(matrix)
        
    for i in range(1, n+1):
        for j in range(1, sum+1):
            
            if j >=coins[i-1]:
                matrix[i][j] = min(1 + matrix[i][j-coins[i-1]], matrix[i-1][j])
                print(matrix)

            else:
                print("here")
                matrix[i][j] = matrix[i-1][j]
                print(matrix)
                
    print(matrix)

                
    return matrix[n][sum]

if __name__ == "__main__":
    coins = [1, 5, 6, 8]
    sum = 11
    n = len(coins)
    
    result = find_coin_change(coins, n, sum)
    print("No. of ways we achieve the sum using coins: ", result)




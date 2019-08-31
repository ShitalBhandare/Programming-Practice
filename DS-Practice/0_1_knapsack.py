
#Code link: https://rextester.com/SDEKA8673

#python 3.5.2

# 0/1 Knapsack Problem


def knapsack(W, wt, val, n):
    
    knapsack = [[ 0 for j in range(W+1)] for i in range(n+1)]
    
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                knapsack[i][j] = 0
            if j < wt[i-1]:
                knapsack[i][j] = knapsack[i-1][j]
            else:
                knapsack[i][j] = max(knapsack[i-1][j], val[i-1]+knapsack[i-1][j-wt[i-1]])
                
    return knapsack[n][W]

if __name__ == "__main__":
    
    wt = [10, 20, 30]
    val = [60, 100, 120]
    W = 50
    
    max_val = knapsack(W, wt, val, len(wt))
    print("Maximum value achieved:", max_val)
    
    


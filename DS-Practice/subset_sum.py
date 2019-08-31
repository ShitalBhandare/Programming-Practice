

#python 3.5.2

def subset_sum(arr, n, sum):
    
    result = [[False for j in range(sum + 1)]for i in range(n+1)]
    
    for i in range(n+1):
        result[i][0] = True
        
    for j in range(sum+1):
        result[0][j] = False
        
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j < arr[i-1]:
                result[i][j] = result[i-1][j]
            else:
                result[i][j] = result[i-1][j] or result[i-1][j-arr[i-1]]

    return result[n][sum]


if __name__ == "__main__":
    
    arr = [1, 2, 3, 4, 5, 6]
    sum = 46
    ret = subset_sum(arr, len(arr), sum)
    if ret:
        print("There exists a subset with given sum")
    else:
        print("There does not exist a subset with given sum")
    
    

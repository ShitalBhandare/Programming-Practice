# Hello World program in Python
    
#python 3.5.2

# Fractional Knapsack Problem


def knapsack(W, wt, val, n):
    
    ratio = []
    for i in range(n):
        ratio.append([val[i]/wt[i], wt[i], val[i]])
    
    # Sorts based on 1st value in list >> Default behavior
    ratio.sort(reverse= True)
    
    totalvalue = 0
    for item in ratio:
        cur_wt = item[1]
        cur_val = item[2]
        
        if W - cur_wt >= 0:
            W -= cur_wt
            totalvalue += cur_val
        else:
            fraction = W / cur_wt
            totalvalue += fraction * cur_val
            W -= cur_wt * fraction
            break
        
    return totalvalue
    

if __name__ == "__main__":
    
    #wt = [10, 20, 30]
    #val = [60, 100, 120]
    #W = 50
    
    wt = [10, 40, 20, 30] 
    val = [60, 40, 100, 120] 
    W = 50
    
    max_val = knapsack(W, wt, val, len(wt))
    print("Maximum value achieved:", max_val)
    
    




'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''
Rain water trapping problem

Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
       | 
   |   || |
_|_||_||||||
'''

def findWater(arr):
    result = 0
    leftmax = 0
    rightmax = 0
    
    l = 0
    r = len(arr) - 1
    
    while(l < r):
        if arr[l] < arr[r]:
            if arr[l] >= leftmax:
                leftmax = arr[l]
            else:
                result += leftmax - arr[l]
            l += 1
        else:
            if arr[r] >= rightmax:
                rightmax = arr[r]
            else:
                result += rightmax - arr[r]
            r -= 1
            
    print("Trapped rain water: ", result, "units")

if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    findWater(arr)
	
	
	
Output:

Trapped rain water:  6 units                                                                                                                   
                                                                                                                                               
                                                                                                                                               
...Program finished with exit code 0                                                                                                           
Press ENTER to exit console.     
/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

/*
Program to find total no of ways to reach to cell using Dynamic Programming
*/


#include <stdio.h>
int N = 4;

void countways(int N, int sol[N][N]){
    
    int i, j;
    
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            sol[i][j] = 0;
        }
    }
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            if((i == 0) || (j == 0)){
                sol[i][j] = 1;
            }
        }
    }
    
    for(i=1; i<N; i++){
        for(j=1; j<N; j++){
            sol[i][j] = sol[i-1][j] + sol[i][j-1];
        }
    }
    
    printf("No of ways to reach the right most bottom element from leftmost top :%d", sol[N-1][N-1]);
}

int main()
{
    int matrix[N][N];
    printf("Enter matrix:\n");
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            scanf("%d", &matrix[i][j]);
        }
    } 
    countways(N, matrix);
}

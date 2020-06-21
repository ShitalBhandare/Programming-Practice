/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
/*
N Queen Problem usimg backtracking
*/


#include <stdio.h>
#include <stdbool.h>

int N = 4;

void printSolution(int N, int sol[N][N]){
    
    int i, j;
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            printf("%d\t", sol[i][j]);
        }
        printf("\n");
    }
}

bool is_safe(int board[N][N], int row, int col){
    
   
    int i, j;
    
    // Check if queen is placed in same row as previous queen.
    for(i=0; i<col; i++){
        if(board[row][i]){
            return false;
        }
    }
    
    // Check if queen is placed in upper left diagonal.
    // row-col=i-j
    
    for(i=row, j=col; i>0 && j>=0; i--, j--){
        if(board[i][j])
            return false;
    }
    
    // Check if queen is placed in lower left diagonal.
    // row+col = i+j
    
    for(i=row, j=col; i<N && j>=0; i++, j--){
        if(board[i][j])
            return false;
    }
    
    return true;
}

bool solveNQueenUtil(int board[N][N], int col){
    
    int i, row;
    
    if(col >= N){
        return true;
    }
    
    for(row=0; row<N; row++){
        
        if(is_safe(board, row, col) == true){
            board[row][col] = 1;
            
            if (solveNQueenUtil(board, col+1) == true){
                return true;
            }
            
            board[row][col] = 0;
        }        
    }
    return false;
}

bool solveNQueen(int board[N][N]){
    
    int i, j;
    
    if(solveNQueenUtil(board, 0) == false){
        printf("Solution does not exit\n");
        return false;
    }
    printf("Solution Matrix:\n");
    printSolution(N, board);
    return true;
}

int main()
{
    int board[N][N], i, j;
    
    /*
    int board[N][N] = { {0, 0, 0, 0},
                      {0, 0, 0, 0},
                      {0, 0, 0, 0},
                      {0, 0, 0, 0} };
    */
    
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            board[i][j] = 0;
        }
    }
    
    solveNQueen(board);
    return 0;
}
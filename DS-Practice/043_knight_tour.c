

/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
/*
knight Tour Problem usimg backtracking
*/


#include <stdio.h>
#include <stdbool.h>

int N = 8;

void printSolution(int N, int sol[N][N]){
    
    int i, j;
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            printf("%d\t", sol[i][j]);
        }
        printf("\n");
    }
}

bool is_safe(int x, int y, int sol[N][N]){
    
    if (x >= 0 && x < N && y >= 0 && y < N && sol[x][y] == -1){
        return true;
    }
    return false;
}

bool solveKnightTourUtil(int x, int y, int nmove, int x_move[N], int y_move[N], int sol[N][N]){
    
    int k, next_x, next_y;
    
    if(nmove == N*N){
        return true;
    }
    
    for(int i=0; i<8; i++){
        
        next_x = x + x_move[i];
        next_y = y + y_move[i];
        
        if(is_safe(next_x, next_y, sol)){
            sol[next_x][next_y] = nmove;
                
            if(solveKnightTourUtil(next_x, next_y, nmove+1, x_move, y_move, sol) == true){
                return true;
            }
            else
            {
                sol[next_x][next_y] = -1;
            }
        }
    }
    return false;
}

bool solveKnightTour(){
    
    int i, j;
    int sol[N][N];
 
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            sol[i][j] = -1;
        }
    }
    
    // Knight's possiblem moves
    
    int x_move[8] = { 1, 2, 2, 1, -1, -2, -2, -1};
    int y_move[8] = { 2, 1, -1, -2, -2, -1, 1, 2};
    
    // Start from 0, 0 
    
    sol[0][0] = 0;
    
    if(solveKnightTourUtil(0, 0, 1, x_move, y_move, sol) == false){
        printf("Solution does not exit\n");
        return false;
    }
    printf("Solution Matrix:\n");
    printSolution(N, sol);
    return true;
}

int main()
{
    solveKnightTour();
    return 0;
}
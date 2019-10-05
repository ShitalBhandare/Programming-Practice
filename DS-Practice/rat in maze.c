
/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

/*
Rat in Maze Problem usimg backtracking
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

bool is_safe(int maze[N][N], int x, int y){
    
    if ((x < N && x >= 0) && (y<N && y>= 0) && maze[x][y]){
        return true;
    }
    return false;
}

bool solvemazeUtil(int maze[N][N], int x, int y, int sol[N][N]){
    
    if((x == N-1) && (y == N-1)){
        sol[x][y] = 1;
        return true;
    }
    
    if(is_safe(maze, x, y) == true){
        sol[x][y] = 1;
        
        if(solvemazeUtil(maze, x+1, y, sol) == true){
            return true;
        }
        
        if(solvemazeUtil(maze, x, y+1, sol) == true){
            return true;
        }
        sol[x][y] = 0;
        return false;
    }
    return false;
}

bool solvemaze(int maze[N][N]){
    
    /*
    int sol[N][N] = { {0, 0, 0, 0},
                      {0, 0, 0, 0},
                      {0, 0, 0, 0},
                      {0, 0, 0, 0} };
    */         
    int sol[N][N];
    int i, j;
    
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            sol[i][j] = 0;
        }
    } 
                    
    
    if(solvemazeUtil(maze, 0, 0, sol) == false){
        printf("Solution does not exit\n");
        return false;
    }
    printf("Solution matrix:\n");
    printSolution(N, sol);
    return true;
}

int main()
{
    int maze[N][N], i, j;
    /*
    int maze[N][N] = { { 1, 0, 0, 0 }, 
                       { 1, 1, 0, 1 }, 
                       { 0, 1, 0, 0 }, 
                       { 1, 1, 1, 1 } }; 
    */
    
    printf("Enter maze matrix:\n");
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            scanf("%d", &maze[i][j]);
        }
    } 
    printf("Maze Mtrix:\n");
    printSolution(N, maze);
    solvemaze(maze);
    return 0;
}

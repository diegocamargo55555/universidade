#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define N 9

typedef struct {
    int grid[N][N];
} SudokuBoard;

void print(SudokuBoard board) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            printf("%d ", board.grid[i][j]);
        printf("\n");
    }
}

int isSafe(SudokuBoard board, int row, int col, int num) {
    for (int x = 0; x <= 8; x++)
        if (board.grid[row][x] == num)
            return 0;

    for (int x = 0; x <= 8; x++)
        if (board.grid[x][col] == num)
            return 0;

    int startRow = row - row % 3, startCol = col - col % 3;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board.grid[i + startRow][j + startCol] == num)
                return 0;

    return 1;
}

volatile int is_solved = 0;
SudokuBoard final_solution;

void solveSudokuParallel(SudokuBoard board, int row, int col, int depth) {
    if (is_solved) return;

    if (row == N - 1 && col == N) {
        #pragma omp critical
        {
            if (!is_solved) {
                is_solved = 1;
                final_solution = board;
            }
        }
        return;
    }

    if (col == N) {
        row++;
        col = 0;
    }

    if (board.grid[row][col] > 0) {
        solveSudokuParallel(board, row, col + 1, depth);
        return;
    }

    for (int num = 1; num <= N; num++) {
        if (isSafe(board, row, col, num) == 1) {
            
            SudokuBoard next_board = board;
            next_board.grid[row][col] = num;

            if (depth < 4) {
                #pragma omp task firstprivate(next_board, row, col, depth) shared(is_solved, final_solution)
                {
                    solveSudokuParallel(next_board, row, col + 1, depth + 1);
                }
            } else {
                solveSudokuParallel(next_board, row, col + 1, depth + 1);
            }
        }
    }
}

int main() {
    SudokuBoard initial_board = {{
        { 5, 3, 0, 0, 7, 0, 0, 0, 0 },
        { 6, 0, 0, 1, 9, 5, 0, 0, 0 },
        { 0, 9, 8, 0, 0, 0, 0, 6, 0 },
        { 8, 0, 0, 0, 6, 0, 0, 0, 3 },
        { 4, 0, 0, 8, 0, 3, 0, 0, 1 },
        { 7, 0, 0, 0, 2, 0, 0, 0, 6 },
        { 0, 6, 0, 0, 0, 0, 2, 8, 0 },
        { 0, 0, 0, 4, 1, 9, 0, 0, 5 },
        { 0, 0, 0, 0, 8, 0, 0, 7, 9 }
    }};

    #pragma omp parallel
    {
        #pragma omp single
        {
            solveSudokuParallel(initial_board, 0, 0, 0);
        }
    }

    if (is_solved)
        print(final_solution);
    else
        printf("No solution exists\n");

    return 0;
}
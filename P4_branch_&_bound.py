# Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for n-queens problem or a graph coloring problem.

def is_safe(board, row, col, N):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_branch_bound(N):
    # Initialize the board
    board = [[0] * N for _ in range(N)]
    
    # Recursive function to place queens
    def place_queens(row):
        # Base case: All queens are placed
        if row == N:
            return True
        
        # Try placing queen in each column of current row
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                # Recur to place queens in the next row
                if place_queens(row + 1):
                    return True
                # Backtrack if placing a queen doesn't lead to a solution
                board[row][col] = 0
        
        return False
    
    # Start with the first row
    if place_queens(0):
        return board
    else:
        return None

# Example usage
N = 8
solution = solve_n_queens_branch_bound(N)
if solution:
    for row in solution:
        print(" ".join("Q" if col == 1 else "-" for col in row))
else:
    print("No solution found.")

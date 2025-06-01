def is_safe(pos, curr_row, col):
    for prev_row in range(curr_row):
        if pos[prev_row] == col or \
           pos[prev_row] - prev_row == col - curr_row or \
           pos[prev_row] + prev_row == col + curr_row:
            return False
    return True

def place_queens(n, row, pos, all_sol):
    if row == n:
        board = []
        for r in range(n):
            row_str = '.' * pos[r] + 'Q' + '.' * (n - pos[r] - 1)
            board.append(row_str)
        all_sol.append(board)
        return

    for col in range(n):
        if is_safe(pos, row, col):
            pos[row] = col
            place_queens(n, row + 1, pos, all_sol)

def solve_n_queens(n):
    sol = []
    pos= [-1] * n 
    place_queens(n, 0, pos, sol)
    return sol

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of queens 1 to 9: "))
        if n < 1 or n > 9:
            print("Please enter a number between 1 and 9.")
        else:
            result = solve_n_queens(n)
            print(f"\nTotal solutions for {n}-Queens: {len(result)}\n")
            for idx, sol in enumerate(result, 1):
                print(f"Solution {idx}:")
                for row in sol:
                    print(row)
                print()
    except ValueError:
        print("Invalid input. Please enter an integer.")


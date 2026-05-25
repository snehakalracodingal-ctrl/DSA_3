def maze_path(row, col):
    
    # If rat reaches destination
    if row == 1 or col == 1:
        return 1

    # Move down + move right
    return maze_path(row - 1, col) + maze_path(row, col - 1)


rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

print("Total paths =", maze_path(rows, cols))
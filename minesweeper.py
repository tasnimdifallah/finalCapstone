# Define the function 'sweeper' that takes a 2D list of mines as input
def sweeper(mines):
    # Create a 2D list of zeros with the same dimensions as the input list 'mines'
    arr = [[0 for _ in range(len(mines[0]))] for _ in range(len(mines))]

    # Loop through each row and column in the 'mines' list
    for current_row, row in enumerate(mines):
        for current_col, value in enumerate(row):
            count = 0
            # Check if each of the neighboring cells contains a mine, and increment the count if it does
            if (current_row-1 >= 0 and current_col-1 >= 0) and mines[current_row-1][current_col-1] == "#":
                count += 1
            if (current_row-1 >= 0) and mines[current_row-1][current_col] == "#":
                count += 1               
            if (current_row-1 >= 0 and current_col+1 < len(row)) and mines[current_row-1][current_col+1] == "#":
                count += 1
            if (current_col-1 >= 0) and mines[current_row][current_col-1] == "#":
                count += 1  
            if (current_col+1 < len(row)) and mines[current_row][current_col+1] == "#":
                count += 1  
            if (current_row+1 < len(mines) and current_col-1 >= 0) and mines[current_row+1][current_col-1] == "#":
                count += 1
            if (current_row+1 < len(mines)) and mines[current_row+1][current_col] == "#":
                count += 1  
            if (current_row+1 < len(mines) and current_col+1 < len(row)) and mines[current_row+1][current_col+1] == "#":
                count += 1
            # If the current cell contains a mine, mark it with a '#'. Otherwise, set it to the count of neighboring mines
            if value == "#":
                arr[current_row][current_col] = "#"
            else:
                arr[current_row][current_col] = count
    # Return the updated list 'arr'
    return arr

# Define a test case as a 2D list of mines
test = [ ["-", "-", "-", "#", "#"],
         ["-", "#", "-", "-", "-"],
         ["-", "-", "#", "-", "-"],
         ["-", "#", "#", "-", "-"],
         ["-", "-", "-", "-", "-"] ]

# Call the 'sweeper' function with the test case and store the result in 'test_result'
test_result = sweeper(test)

# Print the result to the console
for row in test_result:
    print(" ".join(str(cell) for cell in row))
    print()  
rows = int(input("Enter Your Height: ")) # Number of rows in the pattern

for i in range(1, rows + 1):
    if i <= rows // 2:  # Print increasing number of '#' for the first half
        print("#" * i)
    else:  # Print decreasing number of '#' for the second half
        print("#" * (rows - i))

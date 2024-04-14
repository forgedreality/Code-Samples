# Validate input
while True:
    try:
        h = int(input('Height: '))
        if h < 1 or h > 8:
            raise ValueError
        break
    except ValueError:
        print("Invalid input.  Please enter a number between 1 and 8.")

# Iterate
for i in range(h):
    # Calc spaces
    n = (h - 1) - i
    print(" " * n, end="")

    # Calc hashes
    m = h - n
    print("#" * m)

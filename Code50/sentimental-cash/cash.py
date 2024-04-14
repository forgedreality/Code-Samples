import cs50 as c

# Keep track of number of coins
totalCoins = 0
# Valid coin values
coins = [0.25, 0.10, 0.05, 0.01]


def main():
    change = -1
    # Get input from user for cash value
    while not (change >= 0):
        change = c.get_float("Gimme a number tho. ")

    if change == 0:
        return 0

    print(countCoins(change))


def countCoins(ch):
    global totalCoins
    global coins

    # Break out if we've reached zero
    if ch == 0:
        return totalCoins

    # Recursively iterate over coins list to find the least amount of coins
    for i in coins:
        if ch - i >= 0:
            totalCoins += 1
            return countCoins(round(ch - i, 2))


if __name__ == "__main__":
    main()

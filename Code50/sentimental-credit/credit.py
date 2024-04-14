import cs50


# Sum digits of number provided
def addDigits(num):
    digits = str(num)
    output = 0

    for i in digits:
        output += int(i)

    return output


if __name__ == "__main__":
    output = "INVALID"

    # Get input from user for CC number
    c = cs50.get_int("Number: ")
    clen = len(str(c))

    # Valid CC lengths
    lengths = [13, 15, 16]

    if clen in lengths:
        count = 0
        n = c
        total = 0
        temp = 0

        while n > 0:
            if count % 2 != 0:
                # Get last ODD digit and multiply by 2
                temp = int(str(n)[-1]) * 2
                # Sum the digits of the above operation and add to evens counter
                total += addDigits(temp)

            else:
                # Get the last EVEN digit
                temp = int(str(n)[-1])
                # Add digit to odds counter
                total += temp

            count += 1
            # Reduce the number we're evaluating by 1
            n = int(n / 10)

        if total % 10 == 0:
            # Get first 2 digits of given number
            firstDigits = int(c / pow(10, clen - 2))

            # Amex - len: 15; Starts with: 34, 37
            # MC - len: 16; Starts with: 51, 52, 53, 54, 55
            # Visa - len 13, 16; Starts with: 4
            if clen == 13 or clen == 16:
                validDigits = [4]

                # Visa just starts with 4, so div our 2 digits by 10 to get the first digit (int value ignores decimal)
                if int(str(firstDigits)[0]) in validDigits:
                    # Valid Amex
                    output = "VISA"

            if clen == 15:
                validDigits = [34, 37]

                if firstDigits in validDigits:
                    # Valid Amex
                    output = "AMEX"

            if clen == 16:
                validDigits = [51, 52, 53, 54, 55]

                if firstDigits in validDigits:
                    # Valid MC
                    output = "MASTERCARD"

    print(output)


# String formatting
# https://www.hackerrank.com/challenges/python-string-formatting/problem
def print_formatted(number):
    # get longest representation for calculating padding between columns
    #width = len(format(number, 'b'))
    width = len("{0:b}".format(number))

    for i in range(1, number + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

    '''
    # OLD VERSION
    # Decimal, Octal, Hexadecimal (capitalized), Binary
    number_formats = ['Decimal', 'Octal', 'Hexadecimal', 'Binary']
    chart = [[None for _ in range(number)] for _ in range(len(number_formats))]

    for i in range(number):
        # decimal
        chart[0][i] = i+1
        # octal
        chart[1][i] = "{:1o}".format(i+1)
        # hexadecimal
        chart[2][i] = "{:1x}".format(i+1).upper()
        # binary
        chart[3][i] = format(i+1, 'b')

    out = ''

    for y in range(number):
        for x in range(len(chart)):
            # add padding
            v = str(chart[x][y])
            c_width = width - len(v)
            out += f'{" " * c_width}'

            out += str(chart[x][y]) + (' ' if x < len(chart) - 1 else '')
            # add line breaks only at the end of lines,
            # and not after the entire iteration
            out += '\n' if x == len(chart) - 1 and y < number - 1 else ''

    print(out)
    '''

print_formatted(10)

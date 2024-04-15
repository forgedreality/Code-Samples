# hourglass
inputarr = [
    [0, -4, -6, 0, -7, -6],
    [-1, -2, -6, -8, -3, -1],
    [-8, -4, -2, -8, -8, -6],
    [-3, -1, -2, -5, -7, -4],
    [-3, -5, -3, -6, -6, -6],
    [-3, -6, 0, -8, -6, -7]
]
# inputarr = [
#     [1, 1, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0],
#     [0, 0, 2, 4, 4, 0],
#     [0, 0, 0, 2, 0, 0],
#     [0, 0, 1, 2, 4, 0]
# ]
# sanitizedarr = []
# hourglasspattern = [[0, 1, 2, 7, 12, 13, 14], [18, 19, 20, 25, 30, 31, 32]]
# hourglasspattern = {
#     0: [0, 1, 2],
#     1: [1],
#     2: [0, 1, 2]
# }
# totals = []

# for s in inputarr:
#     for n in s:
#         sanitizedarr.append(n)

# print(sanitizedarr)

largestHourglass = float('-inf')
hourglassRecord = []
for row in range(4):
    for col in range(4):
        current = inputarr[row][col] + inputarr[row][col+1] + inputarr[row][col+2] + inputarr[row+1][col+1] + inputarr[row+2][col] + inputarr[row+2][col+1] + inputarr[row+2][col+2]
        print(current)
        if current > largestHourglass:
            largestHourglass = current
            hourglassRecord = [f'{inputarr[row][col]} {inputarr[row][col+1]} {inputarr[row][col+2]}', f'{inputarr[row+1][col+1]}', f'{inputarr[row+2][col]} {inputarr[row+2][col+1]} {inputarr[row+2][col+2]}']
        # totals.append(inputarr[row][col] + inputarr[row][col+1] + inputarr[row][col+2] + inputarr[row+1][col+1] + inputarr[row+2][col] + inputarr[row+2][col+1] + inputarr[row+2][col+2])

print(largestHourglass)
print(hourglassRecord[0])
print(hourglassRecord[1])
print(hourglassRecord[2])





#         for h in hourglasspattern:
#             temp = 0
#             for n in range(len(h)):
#                 print(sanitizedarr[h[n]])
#                 temp += sanitizedarr[h[n]]
#                 h[n] += 1

#             totals.append(temp)

# print(totals)
# print(max(totals))

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    '''
        n = number of chapters
        k = max problems per page
        arr = list of problems per chapter
    '''
    page = 1
    count = 0

    for chapter in range(len(arr)):
        probs_in_chapter = arr[chapter]
        num_full_pages, leftover_probs = divmod(probs_in_chapter, k)

        total_pages = num_full_pages + (1 if leftover_probs else 0)
        problems_in_chapter = iter(range(1, arr[chapter] + 1))

        for _ in range(total_pages):
            probs_on_page = [next(problems_in_chapter, None) for _ in range(k)]
            if page in probs_on_page:
                count += 1
            page += 1

    print(count)
    return count


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     arr = list(map(int, input().rstrip().split()))

#     result = workbook(n, k, arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()


workbook(25, 10, [1, 29, 94, 15, 87, 100, 20, 55, 100, 45, 82, 80, 100, 100, 3, 53, 100, 2, 100, 100, 100, 100, 100, 100, 1])
# workbook(10, 5, [3, 8, 15, 11, 14, 1, 9, 2, 24, 31])

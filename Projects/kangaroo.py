def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        return("YES")
    if v2 > v1 or v1 == v2:
        return("NO")
    elif (x1 - x2)%(v2 - v1) == 0:
        return("YES")

    return("NO")


# '''
# x1 + y * v1 = x2 + y * v2 where "y" is number of jumps... so if (x1 - x2) % (v2 - v1) == 0
# '''
#     if x1 == x2:
#         return("YES")

#     elif x1 > x2:
#         return(jump(x1, x2, v1, v2))

#     else:
#         return(jump(x2, x1, v2, v1))


print(kangaroo(43, 2, 70, 2))
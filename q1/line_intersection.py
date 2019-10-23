

def intersection(x1, x2, x3, x4):
    # swap the numbers if the first is bigger than the second
    if x3 > x4:
        x3, x4 = x4, x3
    if x1 > x2:
        x1, x2 = x2, x1
    if x4 > x2:
        return x2 <= x4 and x2 >= x3
    return x4 <= x2 and x4 >= x1


# print(intersection(8, 5, 9, 6))

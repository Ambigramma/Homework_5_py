def summ(a, b):
    if a == 0:
        return b
    return summ(a-1, b+1)

print(summ(1, 2))
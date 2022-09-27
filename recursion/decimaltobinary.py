def decimaltobinary(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimaltobinary(n//2)


print(decimaltobinary(13))

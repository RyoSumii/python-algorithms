def sumofdigits(n):
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumofdigits(n // 10)


print(sumofdigits(1234))

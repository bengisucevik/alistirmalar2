def topla(n):
    if n==0:
        return 0
    else:
        return n+topla(n-1)

print(topla(10))

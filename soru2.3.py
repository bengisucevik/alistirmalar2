def carpım(n):
    if n==1:
        return 1
    else:
        return n*carpım(n-1)

print(carpım(4))

def f(n):
    if n<2:
        return 0
    elif n==2:
        return 1
    else:
        return f(n-3)+f(n/2)+f(n/4)
print(f(134))




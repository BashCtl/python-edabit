def arithmetic_operation(n):
    n = n.replace(" ", "")
    try:
        return eval(n)
    except:
        return -1


print(arithmetic_operation("12 + 12"))

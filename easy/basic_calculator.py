def calculator(num1, operator, num2):
    try:
        return int(eval("num1{}num2".format(operator)))
    except:
        return "Can't divide by 0!"


print(calculator(2, "+", 2))
print(calculator(4, "/", 2))

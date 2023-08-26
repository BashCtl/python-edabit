def stock_picker(lst):
    profit = max([max(lst[i + 1:]) - lst[i] for i in range(len(lst) - 1)])
    return profit if profit > 0 else -1


print(stock_picker([44, 30, 24, 32, 35, 30, 40, 38, 15]))
print(stock_picker([10, 12, 4, 5, 9]))
print(stock_picker([14, 20, 4, 12, 5, 11]))
print(stock_picker([80, 60, 10, 8]))

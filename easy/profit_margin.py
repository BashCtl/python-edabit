def profit_margin(cost_price, sale_price):
    profit = ((sale_price - cost_price) / sale_price) * 100
    return "{}%".format(round(profit, 1))


print(profit_margin(28, 39))
print(profit_margin(50, 50))
print(profit_margin(33, 84))

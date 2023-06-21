def profit(info):
    return round((info['sell_price'] - info['cost_price']) * info['inventory'])


print(profit({
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
}))

print(profit({
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
}))

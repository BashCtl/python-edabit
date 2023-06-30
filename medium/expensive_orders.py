def expensive_orders(orders, cost):
    return {k: v for k, v in orders.items() if v > cost}


print(expensive_orders({ "a": 3000, "b": 200, "c": 1050 }, 1000))
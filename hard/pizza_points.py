def pizza_points(customers, min_orders, min_price):
    func = lambda item: len([i for i in item[1] if i >= min_price]) >= min_orders
    d = dict(filter(func, customers.items()))
    return sorted(d.keys())


customers = {
    "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
    "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
}

print(pizza_points(customers, 5, 20))

def get_total_price(groceries):
    return round(sum([item["price"] * item["quantity"] for item in groceries]),1)


products = [
    {"product": "Milk", "quantity": 1, "price": 1.50},
    {"product": "Cereals", "quantity": 1, "price": 2.50}
]

print(get_total_price(products))

products2 = [
    {"product": "Chocolate", "quantity": 1, "price": 0.10},
    {"product": "Lollipop", "quantity": 1, "price": 0.20}
]

print(get_total_price(products2))

def get_budgets(lst):
    budgets = [person["budget"] for person in lst]
    return sum(budgets)


print(get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]))
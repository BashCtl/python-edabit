from collections import OrderedDict


def count_datatypes(*args):
    result = OrderedDict()
    result["int"] = 0
    result["str"] = 0
    result["bool"] = 0
    result["list"] = 0
    result["tuple"] = 0
    result["dictionary"] = 0
    for item in args:
        if type(item) == int:
            result["int"] = result.get("int") + 1
        if type(item) == str:
            result["str"] = result.get("str") + 1
        if type(item) == bool:
            result["bool"] = result.get("bool") + 1
        if type(item) == list:
            result["list"] = result.get("list") + 1
        if type(item) == tuple:
            result["tuple"] = result.get("tuple") + 1
        if type(item) == dict:
            result["dictionary"] = result.get("dictionary") + 1

    return list(result.values())


print(count_datatypes(1, 45, "Hi", False))
print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1))
print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23))

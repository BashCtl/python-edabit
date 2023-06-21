import math


def end_corona(recovers, new_cases, active_cases):
    result = active_cases / (recovers - new_cases)
    return math.ceil(result)


print(end_corona(4000, 2000, 77000))
print(end_corona(3000, 2000, 50699))

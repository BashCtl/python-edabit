import math


def twins(age, distance, velocity):
    earth_years = (distance / velocity) * 2
    jill_age = earth_years + age
    gamma = math.sqrt(1 - velocity * velocity)
    jack_age = gamma * earth_years + age
    return "Jack's age is {:.1f}, Jill's age is {:.1f}".format(jack_age, jill_age)


print(twins(20, 10, 0.4))

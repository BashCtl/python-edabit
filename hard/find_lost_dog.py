"""
Find the Lost Dog

0 represents the dog.
Each list represents a house and each 1 represents an empty room.
Return the house and the room where it is located, there can be only one dog lost per building.
Examples
lost_dog([1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
➞ "Dog not found!"

lost_dog([1, 1, 1, 1, 1, 1],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
➞ {"Dog1": "House (2) and Room (1)", "Dog2": "House (3) and Room (2)"}

lost_dog([1, 1, 1, 1, 1, 0],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 0, 1, 1, 1])
➞ {"Dog1": "House (1) and Room (6)", "Dog2": "House (2) and Room (1)", "Do

"""


def lost_dog(*args):
    result = dict()
    dog = 0
    for i, house in enumerate(args):
        for index, room in enumerate(house):
            if room == 0:
                dog += 1
                result.update({"Dog{}".format(dog): "House ({0}) and Room ({1})".format(i+1, index+1)})
    if dog == 0:
        return "Dog not found!"
    return result


print(lost_dog([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]))
print(lost_dog([1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]))

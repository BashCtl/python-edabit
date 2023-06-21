class player():

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    # complete function

    def get_age(self):
        return "{} is age {}".format(self.name, self.age)

    # complete function

    def get_height(self):
        return "{} is {}cm".format(self.name, self.height)

    # complete function

    def get_weight(self):
        return "{} weighs {}kg".format(self.name, self.weight)
# complete function

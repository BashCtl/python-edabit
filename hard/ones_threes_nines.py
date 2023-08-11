class ones_threes_nines:

    def __init__(self, num):
        self.nines = num // 9
        self.threes = (num - self.nines * 9) // 3
        self.ones = (num - self.nines * 9 - self.threes * 3) // 1
        self.answer = "nines:{}, threes:{}, ones:{}".format(self.nines, self.threes, self.ones)


otn = ones_threes_nines(5)
print(otn.answer)

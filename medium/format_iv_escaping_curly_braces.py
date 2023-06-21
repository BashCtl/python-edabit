import unittest

a = "John"
b = "Joe"
template = r"My best friend is {{{}}}."


class Test(unittest.TestCase):

    def test1(self):
        self.assertEquals(template.format(0).format("John", "Joe", "Edabit", "Pikachu"), "My best friend is John.")

    def test2(self):
        self.assertEquals(template.format(1).format("John", "Joe", "Edabit", "Pikachu"), "My best friend is Joe.")

    def test3(self):
        self.assertEquals(template.format(2).format("John", "Joe", "Edabit", "Pikachu"), "My best friend is Edabit.")
    def test4(self):
        self.assertEquals(template.format(3).format("John", "Joe", "Edabit", "Pikachu"), "My best friend is Pikachu.")




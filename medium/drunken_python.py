def int_to_str(num):
    return '{}'.format(num)


def str_to_int(num):
    return int(num)


import unittest


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(str_to_int('4'), 4)

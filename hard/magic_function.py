class Magic:

    def replace(self, s, old, new):
        return s.replace(old, new)

    def str_length(self, s):
        return len(s)

    def trim(self, s):
        return s.strip()

    def list_slice(self, lst: list, t: tuple):
        lst = lst[t[0]-1:t[1]]
        return lst if len(lst) > 0 else -1


magic = Magic()

print(magic.replace("AzErty-QwErty", "E", "e"))
print(magic.str_length("hello world"))
print(magic.trim("      python is awesome      "))
print(magic.list_slice([1, 2, 3, 4, 5], (2, 4)))
print(magic.list_slice([1, 2, 3, 4, 5], (-1, 4)))
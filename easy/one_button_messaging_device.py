def how_many_times(msg):
    return sum([1 if s == 'a' else ord(s) - ord('a') +1 for s in msg])


print(how_many_times("abde"))
print(how_many_times("azy"))
print(how_many_times("qudusayo"))
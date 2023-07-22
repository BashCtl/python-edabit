def sock_merchant(lst):
    return sum([lst.count(item)//2 for item in set(lst)])


print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]))
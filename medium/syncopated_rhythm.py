def has_syncopation(s):
    return any([s[i] == "#" for i in range(1, len(s), 2)])


print(has_syncopation(".#.#.#.#"))
print(has_syncopation("#.#...#."))
print(has_syncopation("#.#.###."))
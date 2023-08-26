def is_correct_aliases(names, aliases):
    return all([nick.split()[0].startswith(name[0])
                and nick.split()[1].startswith(name[0])
                for name, nick in zip(names, aliases)])


print(is_correct_aliases(["Adrian M.", "Harriet S.", "Mandy T."],
                         ["Amazing Artichoke", "Hopeful Hedgehog", "Marvelous Mouse"]))

print(is_correct_aliases(["Beth T."], ["Brandishing Mimosa"]))
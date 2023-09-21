import itertools
import re


def clean_up(files, sort):
    result = []
    for f in files:
        prefix, suffix = f.split('.')

        group = [i for i in files if (i.startswith(prefix) if sort == 'prefix' else i.endswith(suffix))]

        if group not in result:
            result.append(group)
    return result


print(clean_up(["ex1.html", "ex2.html", "ex1.js", "ex2.js"], "prefix"))
print(clean_up(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "suffix"))
print(clean_up(['project1.html', 'project2.html', 'project1.css', 'project2.css', 'project1.js', 'project2.js'],
               'suffix'))

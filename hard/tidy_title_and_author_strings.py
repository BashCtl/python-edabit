def tidy_books(lst):
    return [[t.strip() for t in book[0].split("-")] for book in lst]


books1 = [
  ["   Death of a Salesman - Arthur Miller    "],
  ["   Macbeth - William Shakespeare    "],
  ["    A Separate Peace - John Knowles     "],
  [" Lord of the Flies - William Golding"],
  ["A Tale of Two Cities - Charles Dickens"]
]
print(tidy_books(books1))

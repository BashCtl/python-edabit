class Pagination:

    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.totalPages = 0
        self.currentPage = 0

    def getItems(self):
        return self.items

    def getPageSize(self):
        return self.pageSize

    def getCurrentPage(self):
        return self.currentPage + 1

    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
        return self

    def nextPage(self):
        if self.currentPage < len(self.items) // self.pageSize:
            self.currentPage += 1
        return self

    def firstPage(self):
        self.currentPage = 0
        return self

    def lastPage(self):
        self.currentPage = len(self.items) // self.pageSize
        return self

    def goToPage(self, page):
        if page > len(self.items) // self.pageSize:
            self.lastPage()
        elif page < 0:
            self.firstPage()
        else:
            self.currentPage = int(page - 1)
        return self

    def getVisibleItems(self):
        current_position = self.currentPage * self.pageSize
        return self.items[current_position:current_position+self.pageSize]


# alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# p = Pagination(alphabetList, 4)
# print(p.getVisibleItems())

p1 = Pagination([None] * 69, 5)

print(p1.nextPage().getCurrentPage())
print(p1.lastPage().getCurrentPage())
print(p1.nextPage().getCurrentPage())
print(p1.prevPage().getCurrentPage())
print(p1.firstPage().getCurrentPage())
print(p1.prevPage().getCurrentPage())
print(p1.goToPage(99).getCurrentPage())
print(p1.goToPage(4).getCurrentPage())
print(p1.goToPage(6.5).getCurrentPage())
print(p1.goToPage(-99).getCurrentPage())

ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p2 = Pagination(ids, 5)
print(p2.getVisibleItems())
print(p2.nextPage().getVisibleItems())
print(p2.nextPage().getVisibleItems())
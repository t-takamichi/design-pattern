from iterator.iterator import Iterator

class BookShelfIterator(Iterator):
    def __init__(self, bookShelf):
        self.__bookShelf = bookShelf
        self.__index = 0

    def hasNext(self):
        return True if self.__index < self.__bookShelf.getLength() else False

    def next(self):
        book = self.__bookShelf.getBookAt(self.__index)
        self.__index += 1
        return book
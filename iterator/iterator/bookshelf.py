from iterator.iterable import Iterable
from iterator.bookshelfiterator import BookShelfIterator

class BookShelf(Iterable):
    def __init__(self, maxSize):
        self.__last = 0
        self.__books = [None] * maxSize

    def getBookAt(self, index):
        return self.__books[index]
    
    def append(self, book):
        self.__books[self.__last] = book
        self.__last += + 1
    
    def getLength(self):
        return self.__last
    
    def iterator(self):
        return BookShelfIterator(self)
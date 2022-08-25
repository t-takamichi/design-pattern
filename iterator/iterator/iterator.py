from abc import ABCMeta, abstractmethod

class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def hasNext(self):
        raise NotImplementedError()

    @abstractmethod
    def next(self):
        raise NotImplementedError()
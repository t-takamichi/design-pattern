from abc import ABCMeta, abstractmethod

class Iterable(metaclass=ABCMeta):
    @abstractmethod
    def iterator(self):
        raise NotImplementedError()
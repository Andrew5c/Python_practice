#!Anaconda/anaconda/python
#coding: utf-8

# insertion, deletion, and random access of array
# assumes int for element array

class MyArray:
    """a simple wrapper around List
    we want this class proform like a List
    """
    def __init__(self, capacity: int):
        # protecded value
        self._data = []
        self._capacity = capacity

    # relize these magic methods to operate our own List like class
    def __getitem__(self, position: int) -> object:
        return self._data[position]

    def __setitem__(self, index: int, value: object):
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        # make the object of the class is iterable
        for item in self._data:
            yield item

    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._capacity:
            return False
        else:
            self._data.insert(index, value)
            return True

    def printAll(self):
        for item in self:
            print(item)


def testMyarray():
    array = MyArray(5)
    array.insert(0,3)
    array.insert(0,4)
    array.insert(1,5)
    assert len(array) == 3
    assert array.delete(1) is True
    array.printAll()

if __name__ == "__main__":
    testMyarray()





# Afshin Masoudi
# CS50p/Problem Set 8/Cookie Jar
class Jar:
    def __init__(self, capacity= 12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError('Invalid capacity')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, number):
        if not isinstance(number, int) or number < 0:
            raise ValueError('Invalid number')
        if self._size + number > self._capacity:
            raise ValueError('Not enough space')
        self._size += number

    def withdraw(self, number):
        if not isinstance(number, int) or number < 0:
            raise ValueError('Invalid number')
        if self._size - number < 0:
            raise ValueError('Not enough cookies')
        self._size -= number

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError('Invalid capacity')
        self._capacity = capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(4)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(4)
    print(jar)

if __name__ == "__main__":
    main()
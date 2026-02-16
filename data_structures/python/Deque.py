# https://contest.yandex.ru/contest/23759/run-report/67773226/
from typing import Tuple, List, Any


class MyError(Exception):
    def __init__(self):
        pass


class Deque:
    def __init__(self, max_n):
        self.array = [None] * max_n
        self.max_n = max_n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_n

    def push_back(self, element):
        if self.is_full():
            raise MyError
        self.array[self.tail] = element
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def push_front(self, element):
        if self.is_full():
            raise MyError
        self.head = (self.head - 1) % self.max_n
        self.array[self.head] = element
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise MyError
        self.tail = (self.tail - 1) % self.max_n
        x = self.array[self.tail]
        self.array[self.tail] = None
        self.size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            raise MyError
        x = self.array[self.head]
        self.array[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


def read_input() -> Tuple[int, int]:
    number_of_commands = int(input())
    deck_size = int(input())
    return number_of_commands, deck_size


def read_commands(deck: Deque, number_of_commands: int) -> List[Any]:
    result = []
    for _ in range(number_of_commands):
        command = input().split()
        try:
            if len(command) == 1:
                output = getattr(deck, command[0])()
                result.append(output)
            else:
                getattr(deck, command[0])(command[1])
        except MyError:
            result.append('error')
    return result


if __name__ == "__main__":
    number_of_commands, deck_size = read_input()
    deck = Deque(deck_size)
    result = read_commands(deck, number_of_commands)

    for item in result:
        print(item)

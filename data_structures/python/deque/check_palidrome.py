from Deque import Deque


def check_palidrome(word: str) -> bool:
    deque = Deque()
    for letter in word:
        deque.addTail(letter)

    while deque.size() > 1:

        letter_front = deque.removeFront()
        letter_tail = deque.removeTail()

        if letter_front != letter_tail:
            return False

    return True

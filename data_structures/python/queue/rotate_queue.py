from Queue import Queue


def rotate(queue: Queue, n: int):
    for _ in range(n):
        item = queue.dequeue()
        queue.enqueue(item)

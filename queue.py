# Очередь (FIFO - First In, First Out) также можно реализовать с помощью списка,
# используя методы `append()` для добавления элемента и `pop(0)` для извлечения элемента.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("dequeue from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Пример использования
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Вывод: 1
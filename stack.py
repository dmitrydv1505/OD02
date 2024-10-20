# Стек (LIFO - Last In, First Out) можно реализовать с помощью списка,
# используя методы `append()` для добавления элемента и `pop()` для извлечения элемента.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Вывод: 2
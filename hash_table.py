# hash_table.py
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.data = [None]*size

    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, number):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                current.value.number = number
                return
            current = current.next
        new_node = Node(key, Contact(key, number))
        new_node.next = self.data[index]
        self.data[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i, node in enumerate(self.data):
            print(f"Index {i}:", end=" ")
            if not node:
                print("Empty")
            else:
                current = node
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()

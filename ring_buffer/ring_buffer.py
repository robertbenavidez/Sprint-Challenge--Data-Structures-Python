from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == None:
            self.current = self.storage.head

        if self.capacity == self.storage.length and self.current == self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.current.next

        elif self.capacity == self.storage.length and self.current == self.storage.tail:
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            self.current = self.storage.head

        elif self.capacity == self.storage.length:
            self.current.insert_after(item)
            self.storage.length += 1
            self.storage.delete(self.current)
            self.current = self.current.next.next

        else:
            self.storage.add_to_tail(item)

    def get(self):
        buffer_items = []
        temp = self.storage.head

        if temp is None:
            return buffer_items
        else:
            while temp is not None:
                buffer_items.append(temp.value)
                temp = temp.next
        return buffer_items


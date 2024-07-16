class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        pre = self.head
        if pre is None:
            return None
        elif pre.next is None:
            self.head = None
            self.tail = None
            self.length = 0
            return pre
        else:
            temp = self.head.next
            while temp.next is not None:
                temp = temp.next
                pre = pre.next
            self.tail = pre
            pre.next = None
            self.length -= 1
            return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        first = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = first.next
        self.length -= 1
        return first

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        first = self.head
        for _ in range(index):
            first = first.next
        return first

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif self.length == 1 or index == self.length - 1:
            return self.pop()
        else:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = remove_node.next
            remove_node.next = None
            self.length -= 1
            return remove_node

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def remove_duplicates(self):
        if self.head is None:
            return None
        value_set = set()
        current = self.head
        prev = None
        while current is not None:
            if current.value in value_set:
                prev.next = current.next
            else:
                value_set.add(current.value)
                prev = current
            current = current.next
        return self

    def binary_to_decimal(self):
        temp = self.head
        binary_num = []
        while temp is not None:
            binary_num.append(temp.value)
            temp = temp.next
        decimal_value = 0
        for i, value in enumerate(reversed(binary_num)):
            decimal_value += value * (2 ** i)
        return decimal_value

    def partition_list(self, x):
        if self.head is None:
            return None
        lower_part = LinkedList(0)
        higher_part = LinkedList(0)
        current = self.head
        while current is not None:
            if current.value < x:
                lower_part.append(current.value)
            else:
                higher_part.append(current.value)
            current = current.next
        if lower_part.head.next is None:
            return higher_part
        elif higher_part.head.next is None:
            return lower_part
        lower_part.tail.next = higher_part.head.next
        higher_part.head = None  # Clear dummy node
        return lower_part

def find_kth_from_end(ll, k):
    fast = ll.head
    slow = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow

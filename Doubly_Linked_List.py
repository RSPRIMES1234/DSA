from typing import Any


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None







class DoublyLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next


    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.length+=1
            return True
        temp=self.tail
        temp.next=new_node
        new_node.prev=temp
        self.tail=new_node
        self.length+=1
        return True

    def pop(self):
        temp=self.head
        if temp is None:
            return None
        if temp.next is None:
            self.head=None
            self.tail=None
            self.length=0
            return temp
        temp=self.tail
        self.tail=temp.prev
        temp.prev=None
        self.tail.next=None
        self.length-=1
        return temp
    def prepend(self,value):
        new_node=Node(value)
        temp=self.head
        while temp is not None:
            new_node.next=temp
            temp.prev=new_node
            self.head=new_node
            self.length+=1
            return True
        self.head=new_node
        self.tail=new_node
        self.length+=1
        return True
    def pop_first(self):
        temp=self.head
        while temp is None:
            return None
        if temp.next is None:
            self.head=None
            self.tail=None
            self.length=0
            return temp
            
        
        self.head=temp.next
        temp.next=None
        self.head.prev=None
        self.length-=1
        return temp
    def get(self,index):
        if index>=self.length or 0>index:
            return None
        if index<self.length/2 :
            Temp=self.head
            for _ in range(index):
                Temp=Temp.next
            return Temp
        Temp=self.tail
        for _ in range(self.length-index-1):
            Temp=Temp.prev
        return Temp
    def set_value(self,index,value):
        a=self.get(index)
        while a is not None:
            a.value=value
            return True
        return False
        # if index>=self.length or 0>index:
        #     return False
        # if index<self.length/2 :
        #     Temp=self.head
        #     for _ in range(index):
        #         Temp=Temp.next
        #     Temp.value=value
        #     return True
        # Temp=self.tail
        # for _ in range(self.length-index-1):
        #     Temp=Temp.prev
        # Temp.value=value
        # return True

    def insert(self,index,value):
        if index==self.length:
            self.append(value)
            return True
        if index>=self.length or 0>index:
            return False
        if index==0 or self.length==0:
            self.prepend(value)
            return True
        if index==self.length-1:
            self.append(value)
            return True
        new_node=Node(value)
        temp=self.get(index)
        temp2=temp.prev
        temp2.next=new_node
        new_node.next=temp
        temp.prev=new_node
        return True
    
    def remove(self,index):
        if index>=self.length or 0>index:
            return None
        Temp=self.head
        if index==0:
            if Temp is None:
                return None
            return self.pop_first()
        temp=self.get(index)
        pre=temp.prev
        pre.next=temp.next
        temp.next.prev=pre
        temp.next=None
        temp.prev=None

        return temp

        
    def swap_first_last(self):
        if self.length==0:
            return False
        first=self.get(0)
        print(first.value)
        last=self.get(self.length-1)
        print(last.value)
        self.head.value=last.value
        self.tail.value=first.value
        return True          



    def reverse(self):
        if self.length==0:
            return True
        temp=self.head
        temp2=self.tail
        self.head=temp2
        self.tail=temp
        while temp2.prev is not None:
            temp=temp2.prev
            temp3=temp2.next
            temp2.prev=temp3
            temp2.next=temp
            temp2=temp2.next
        
        return True










dll=DoublyLinkedList(0)
# print(dll.pop().value)
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(100)
dll.append(4)
dll.append(5)
# dll.insert(3,9)

# print(dll.pop())
# dll.prepend(100)
# print(dll.pop_first())
# print(dll.get(3))
# # dll.set_value(0,200)
# # dll.remove(3)
# dll.swap_first_last()
dll.reverse
dll.print_list()

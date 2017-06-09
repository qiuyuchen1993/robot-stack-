from src.linked_list import *
class Node(object):
    """ A Node in a Linked List
    """
    
    __next = None
    __element = None
    
    
    def __init__(self, element=None):
        self.__next = None
        self.__element = element
    
    def get_next(self):
        return self.__next

    def get_element(self):
        return self.__element

    def set_next(self, next):
        self.__next = next

    def set_element(self, element):
        self.__element = element

    def __repr__(self):
        return "node: " + str(self.get_element())


class stack(object):
    def __init__(self,size, node=None):
        link= LinkedList()
        self.__first = node
        self.__my_stack = link
        self.__size=size
        self.__length=link.get_size()
        
    def head(self):
        return self.__first
    
    def pushing(self, node):
        if(self.__size==self.__length):
            print("full")
        else:
            node.set_next(self.head())
            self.__first = node
        
    def popping(self):
        self.__first = self.__first.get_next()

        
    def get_top(self):
        return self.__first
    
    def get_stack(self):
        return self.__my_stack
    
    def get_length(self):
        return self.__length
    

    
    def __repr__(self):
        result = ""
        current = self.__first
        while not (current is None):
            result += " -> " + str(current)
            current = current.get_next()
        return result
    
'''
l = stack(1)
l.pushing(Node("s"))
l.pushing(Node("toto"))
l.pushing(Node(2))
l.pushing(Node("toto"))
l.pushing(Node("toto"))
print(l)
print(l.head())
l.popping()
print(l)
l.popping()
print(l)
l.popping()
print(l)
print(str(l.get_top()))
print(str(l.get_top())=="node: toto")'''

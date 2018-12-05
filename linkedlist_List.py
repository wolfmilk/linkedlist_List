#-------------------------------------------------------------------------------
# Madani Djallil
# COP 4533
# Design and implement an experiment that will compare the performance of a Python list with a list implemented as a linked list.
#
#-------------------------------------------------------------------------------
import time
class Node:
    def __init__(self, value):
        self.value = value    
        self.next = None      
        self.prev = None      
class LinkedList():
    def __init__(self, iterable=None):
        self.sentinel = Node(None)           
        self.sentinel.next = self.sentinel   
        self.sentinel.prev = self.sentinel   
        self.__len = 0                       
        if iterable is not None:
            self += iterable        
    def get_node(self, index):
        node = sentinel = self.sentinel 
        i = 0                              
        while i <= index:                        
            node = node.next               
            if node == sentinel:   
                break
            i += 1
        if node == sentinel:              
            node = None
        return node     
    def __delitem__(self, index):
        node = self.get_node(index)     
        if node:                         
            node.prev.next = node.next  
            if node.next:                
                node.next.prev = node.prev     
            node.prev = None       
            node.next = None
            node.value = None
            self.__len -= 1             
class Stopwatch:  
    def __init__(self):
        self.__start = 0.0
        self.__stop = 0.0
        self.__duration = 0.0
    def start(self): 
        self.__start = time.time()
        return self
    def stop(self): 
        self.__stop = time.time()
        self.__duration = self.__stop - self.__start
        return self.__duration
    def duration(self):
        return self.__duration   
class Profiler:
    def __init__(self, size): 
        self.size = size
        self.list = None
        self.linked_list = None
        self.sw_create_list = Stopwatch()
        self.sw_create_linked_list = Stopwatch()
        self.sw_pop_list = Stopwatch()
        self.sw_pop_linked_list = Stopwatch()
    def create_list(self): 
        self.sw_create_list.start()
        self.list = [i for i in range(self.size)]
        self.sw_create_list.stop()
    def create_linked_list(self):
        self.sw_create_linked_list.start()
        self.linked_list = LinkedList()
        for value in self.list:
            self.linked_list.append(value)
        self.sw_create_linked_list.stop()
    def pop_list(self):
        self.sw_pop_list.start()
        for i in range(self.size):
            del self.list[0]
        self.sw_pop_list.stop()
    def pop_linked_list(self): 
        self.sw_pop_linked_list.start()
        for i in range(self.size): 
            del self.linked_list[0]
        self.sw_pop_linked_list.stop()
    def report(self):
        print("%6s %10d" % ("Size", self.size))
        print("%6s %10s %10s %10s" % ("Type", "    Create", "Pop", "Total")) 
        print("%6s %10.2f %10.2f %10.2f" % ("List", self.sw_create_list.duration(), \
                self.sw_pop_list.duration(), self.sw_create_list.duration() + self.sw_pop_list.duration()))
        print("%6s %10.2f %10.2f %10.2f" % ("Linked", self.sw_create_linked_list.duration(), \
                self.sw_pop_linked_list.duration(), self.sw_create_linked_list.duration() + \
                self.sw_pop_linked_list.duration()))
        print
    def run(self):
        self.create_list()
        self.pop_list()
        self.create_linked_list()
        self.pop_linked_list()
        self.report()
if __name__ == '__main__':
    Profiler(10000).run()
    Profiler(20000).run()
    print ("End.")

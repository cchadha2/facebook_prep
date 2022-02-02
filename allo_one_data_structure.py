from math import inf

class Node:
    
    def __init__(self, next=None, prev=None):
        self.data = set()
        self.next = next
        self.prev = prev
        
    def __len__(self):
        return len(self.data)

    def __contains__(self, key):
        return key in self.data
    
    def __bool__(self):
        return bool(self.data)
    
    def __repr__(self):
        return f"Node(data={self.data})"
    
    def remove(self, key):
        self.data.remove(key)
        
    def add(self, key):
        self.data.add(key)
        
    def get_any(self):
        if self.data:
            val = self.data.pop()
            self.data.add(val)
            return val
        
        return None
    
    
class DoublyLinkedList:
    
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
        
    def insert_after(self, node):
        temp = node.next
        node.next = Node(next=temp, prev=node)
        temp.prev = node.next
        return node.next
        
    def insert_before(self, node):
        return self.insert_after(node.prev)
        
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        
    def get_dummy_head(self):
        return self.head
        
    def get_dummy_tail(self):
        return self.tail
    
    def get_head(self):
        return self.head.next
        
    def get_tail(self):
        return self.tail.prev
    
    
class AllOne:

    def __init__(self):
        self.list = DoublyLinkedList()
        self.counts_to_nodes = {0: self.list.get_dummy_head()}
        self.words_to_counts = {}
        

    def inc(self, key: str) -> None:
        prev_count = self.words_to_counts.setdefault(key, 0)
        
        self.words_to_counts[key] += 1
        curr_count = self.words_to_counts[key]
        #print(self.counts_to_nodes, key, curr_count, prev_count)
        
        if not curr_count in self.counts_to_nodes:
            node = self.list.insert_after(self.counts_to_nodes[prev_count])
            self.counts_to_nodes[curr_count] = node
            
        self.counts_to_nodes[curr_count].add(key)
            
        if prev_count:
            self._delete_key(prev_count, key)
            

    def dec(self, key: str) -> None:
        prev_count = self.words_to_counts.setdefault(key, 0)
        if prev_count:
            
            self.words_to_counts[key] -= 1
            curr_count = self.words_to_counts[key]
            
            if curr_count and (not curr_count in self.counts_to_nodes):
                node = self.list.insert_before(self.counts_to_nodes[prev_count])
                self.counts_to_nodes[curr_count] = node
                
            self.counts_to_nodes[curr_count].add(key) 
            self._delete_key(prev_count, key)
                
                

    def getMaxKey(self) -> str:
        tail = self.list.get_tail()
        return tail.get_any() if tail else ""
        

    def getMinKey(self) -> str:
        head = self.list.get_head()
        return head.get_any() if head else ""
        
        
    def _delete_key(self, count, key):
        node = self.counts_to_nodes[count]
        node.remove(key)
        
        if not node:
            self.list.remove(node)
            del self.counts_to_nodes[count]
        
        
        
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

class Node():
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cach={}
        self.right,self.left=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left

        
    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev
     

    
    def insert(self,node):
        prev,nxt=self.right.prev,self.right
        prev.next=nxt.prev=node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cach:
            self.remove(self.cach[key])
            self.insert(self.cach[key])
            return self.cach[key].val
        else:
            return -1

    
    def put(self, key: int, value: int) -> None:
        if key in self.cach:
            self.remove(self.cach[key])
        self.cach[key]=Node(key,value)
        self.insert(self.cach[key])
        if len(self.cach)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cach[lru.key]

    


    
class FreqStack:

    def __init__(self):
        self.dic={}
        self.maxCount=0
        self.stack={}
        

    def push(self, val: int) -> None:
        valCnt=1+self.dic.get(val,0)
        self.dic[val]=valCnt
        if valCnt>self.maxCount:
            self.maxCount=valCnt
            self.stack[valCnt]=[]
        self.stack[valCnt].append(val)
        
        
        
        

    def pop(self) -> int:
        res = self.stack[self.maxCount].pop()
        self.dic[res]-=1
        if not self.stack[self.maxCount]:
            self.maxCount-=1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
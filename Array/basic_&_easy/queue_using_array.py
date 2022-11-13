class MyQueue:
    def __init__(self):
        self.s=[]
    
    #Function to push an element x in a queue.
    def push(self, x):
        self.s.append(x)
        return s
         
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self):
        if len(self.s)==0:
            return -1
        else:
            return self.s.pop(0)
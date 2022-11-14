#Function to push an integer into the stack1.
def push1(a,x):
    #code here
    a.insert(0,x)
    
#Function to push an integer into the stack2.
def push2(a,x):
    #code here
    a.insert(len(a),x)
    
#Function to remove an element from top of the stack1.    
def pop1(a):
    #code here
    if len(a):
        return a.pop(0)
    
#Function to remove an element from top of the stack2.    
def pop2(a):
    #code here
    return a.pop(-1)
    
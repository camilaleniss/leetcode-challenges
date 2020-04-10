class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.index_last = -1
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        min_number = x

        if len(self.stack)!=0:
            prevmin = self.topNode().getMinVal()
            if prevmin < x :
                min_number = prevmin

        node = StackNode(x, min_number)
        self.stack.append(node)
        self.index_last = self.index_last+1

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.index_last = self.index_last -1
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.index_last].getValue()

    def topNode(self):
        return self.stack[self.index_last]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.topNode().getMinVal()

class StackNode(object):

    def __init__(self, value, min):
        self.value = value
        self.min = min

    def getMinVal(self):
        return self.min

    def getValue(self):
        return self.value
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

stack = MinStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(-1)
stack.pop()
print(stack.getMin())
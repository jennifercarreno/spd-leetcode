class MinStack(object):

    def __init__(self):
        # creates empty array?
        self.stack = []
        self.min = float("inf")
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        # appends to array
        
        
        # keeping track of min: if the array is empty then val is min
        # if not empty, compare current min with val 
        
        # checks if stack is empty
        if len(self.stack) == 0:
            self.min = val  # if empty then the first value is the min
            self.stack.append(val)
        else:  # if stack is not empty
            if val < self.min: # check to see if val is smaller than our current min
                self.min = val # if it is then val = min
                self.stack.append(val)
            else: 
                self. stack.append(val) # if not then min stays the same
        

    def pop(self):
        """
        :rtype: None
        """
        # removes from array (top element)
       
        
        #keeping track of min: if top element is min, then check the other values and find the new min
        
        top_element = self.stack[len(self.stack) - 1]
        
        if top_element == self.min: 
            self.stack.pop()
            self.min = min(self.stack)
        else:
            self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        # gets the last item from array
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        # reads array and returns the smalles number
        # sorting doesnt work bc then it stays sorted and messes with the order of elements
        # instead just keep track of min
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
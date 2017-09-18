'''
Problem:
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''
# implement the stack


class SpecialStack(object):
    # initialize the object and create the stack.

    def __init__(self):
        self.stack = []

    # create a string version of the stack
    def __str__(self):
        string = "["
        for item in self.stack:
            string += "{}, ".format(item[0])
        return string + "]"

    # create push
    def push(self, item):
        # if the length of the stack is 0, then minimum will also be the item
        if len(self.stack) == 0:
            # addToStack will have our value at position 0 and our minimum at
            # position 1 (item, stack minimum)
            addToStack = (item, item)
            self.stack.append(addToStack)
        # check if the new value is less than the minimum by checking the last
        # values minimum
        elif item < self.stack[-1][1]:
            addToStack = (item, item)
            self.stack.append(addToStack)
        # if it is not the minimum, then just add it with the previous minimum
        else:
            addToStack = (item, self.stack[-1][1])
            self.stack.append(addToStack)

    def pop(self):
        # if there is no values to pop, return none
        if len(self.stack) == 0:
            return None
        # pop off the last element in the stack
        # sett popped value for reinting purposes
        popped_value = self.stack[-1][0]
        self.stack.pop()
        return popped_value

    def top(self):
        # return the last element in the stack i.e the top of the stack
        return self.stack[-1][0]

    # return the minimum value
    def getMin(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]

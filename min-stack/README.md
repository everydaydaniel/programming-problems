# Minimum stack
## Problem
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.
- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.

# Solution
In this method we handled the minimum values entirely in our push method. Instead of holding the minimum value as a separate variable just hold it alongside your value in a tuple. When we push values in we
insert them as (item, minimum value). To do this we have three conditions.
### Stack is empty
If the stack is empty then the obvious minimum value is the first element.
We insert the values as (value, value)
### The Stack is not empty and new value is new minimum
If our new value is less than the current minimum value (by accessing
the last value in the stack and comparing it to the previous
minimum value) then we insert the new value as (value, value)
### The Stack is not empty and new value is not a new minimum
In this final case we just add it as (value, previous minimum)

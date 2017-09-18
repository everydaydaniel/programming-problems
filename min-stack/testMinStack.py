import unittest
import minStack
from random import randint

stack = minStack.SpecialStack()
values = [22, 1, 4, 5, 6, 7, 5, 3, 11, 15]
for value in values:
    stack.push(value)


class TestMinStack(unittest.TestCase):

    def test_push(self):
        print("\n\ntest push")
        print("Stack: {}".format(stack))
        for i in range(5):
            randVal = randint(5, 10)
            stack.push(randVal)
            self.assertEqual(randVal, stack.top())
            print("pushed: {} == top: {}".format(
                randVal, stack.top()
            ))
        print(stack)

    def test_min(self):
        print("\ntest min")
        min_val = -4
        stack.push(min_val)
        stack.push(100)
        print("Stack: {}".format(stack))
        self.assertEqual(min_val, stack.getMin())
        print("minimum: {}".format(stack.getMin()))
        for i in range(8):
            stack.pop()
        print("Stack: {}".format(stack))
        print("minimum: {}".format(stack.getMin()))
        self.assertEqual(1, stack.getMin())

if __name__ == '__main__':

    unittest.main()

import unittest
import stacks


class test_stacks(unittest.TestCase):

	def test_stack(self):

		#check stack_object is of class Stack
		self.assertIsInstance(stacks.Stack(), stacks.Stack)

		#check Stacks attribute items is of class list
		self.assertIsInstance(stacks.Stack().items, list)

	def test_stack_operation(self):
		
		my_stack = stacks.Stack()
		my_stack.push(1)

		#check methods all work
		self.assertEqual(my_stack.items[0], 1)
		self.assertEqual(my_stack.peek(), 1)
		self.assertEqual(my_stack.size(), 1)
		self.assertEqual(my_stack.is_empty(), False)
		self.assertEqual(my_stack.pop(), 1)

	def test_is_balanced(self):

		#check is_balanced function works
		self.assertEqual(stacks.is_balanced(stacks.Stack(), '{()}'), True)
		self.assertEqual(stacks.is_balanced(stacks.Stack(), '{()'), False)

        #checks that an error is raised when expected
		with self.assertRaises(ValueError):

			stacks.is_balanced(stacks.is_balanced(stacks.Stack(), '{{f'))


if __name__ == '__main__':
	unittest.main() 



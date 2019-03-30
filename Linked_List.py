class Node(object):

	def __init__(self, data, next = None):
		self.next = next
		self.data = data

	def __str__(self):
		return self.data

class LinkedList(object):

	def __init__(self, head = None):
		self.head = head

	def __len__(self):
		curr = self.head
		counter = 0
		while curr is not None:
			counter += 1
			curr = curr.next
		return counter

	def insert_at_start(self, data):
		if data is None:
			return None
		node = Node(data, self.head)
		self.head = node
		return node

	def append(self, data):
		if data is None:
			return None

		node = Node(data)
		if self.head is None:
			self.head = node
			return node

		curr_node = self.head
		while curr_node is not None:
			curr_node = curr_node.next

		curr_node = node

		return node

	def find(self, data):
		if data is None:
			return None
		curr_node = self.head
		while curr_node is not None:
			if curr_node.data == node.data:
				return curr_node
			curr_node = curr_node.next

		return None

	def delete(self, data):
		if data is None:
			return
		if self.head is None:
			return
		if self.head.data == data:
			self.head = self.head.next
			return
		prev_node = self.head
		curr_node = self.head.next
		while curr_node is not None:
			if curr_node.data == node.data:
				prev_node.next = curr_node.next
			prev_node = curr_node
			curr_node = curr_node.next

	def print_list(self):
		curr_node = self.head
		while curr_node is not None:
			print(curr_node.data)
			curr_node = curr_node.next

	def get_all_data(self):
		data = []
		curr_node = self.head
		while curr_node is not None:
			data.append(curr_node.data)
			curr_node = curr_node.next
		return data

# %%writefile test_linked_list.py
from nose.tools import assert_equal


class TestLinkedList(object):

	def test_insert_at_start(self):
		print('Test: insert_at_start on an empty list')
		linked_list = LinkedList(None)
		linked_list.insert_at_start(10)
		assert_equal(linked_list.get_all_data(), [10])

		print('Test: insert_at_start on a None')
		linked_list.insert_at_start(None)
		assert_equal(linked_list.get_all_data(), [10])

		print('Test: insert_at_start general case')
		linked_list.insert_at_start('a')
		linked_list.insert_at_start('bc')
		assert_equal(linked_list.get_all_data(), ['bc', 'a', 10])

		print('Success: test_insert_at_start\n')

	def test_append(self):
		print('Test: append on an empty list')
		linked_list = LinkedList(None)
		linked_list.append(10)
		assert_equal(linked_list.get_all_data(), [10])

		print('Test: append a None')
		linked_list.append(None)
		assert_equal(linked_list.get_all_data(), [10])

		print('Test: append general case')
		linked_list.append('a')
		linked_list.append('bc')
		assert_equal(linked_list.get_all_data(), [10, 'a', 'bc'])

		print('Success: test_append\n')

	def test_find(self):
		print('Test: find on an empty list')
		linked_list = LinkedList(None)
		node = linked_list.find('a')
		assert_equal(node, None)

		print('Test: find a None')
		head = Node(10)
		linked_list = LinkedList(head)
		node = linked_list.find(None)
		assert_equal(node, None)

		print('Test: find general case with matches')
		head = Node(10)
		linked_list = LinkedList(head)
		linked_list.insert_at_start('a')
		linked_list.insert_at_start('bc')
		node = linked_list.find('a')
		assert_equal(str(node), 'a')

		print('Test: find general case with no matches')
		node = linked_list.find('aaa')
		assert_equal(node, None)

		print('Success: test_find\n')

	def test_delete(self):
		print('Test: delete on an empty list')
		linked_list = LinkedList(None)
		linked_list.delete('a')
		assert_equal(linked_list.get_all_data(), [])

		print('Test: delete a None')
		head = Node(10)
		linked_list = LinkedList(head)
		linked_list.delete(None)
		assert_equal(linked_list.get_all_data(), [10])

		print('Test: delete general case with matches')
		head = Node(10)
		linked_list = LinkedList(head)
		linked_list.insert_at_start('a')
		linked_list.insert_at_start('bc')
		linked_list.delete('a')
		assert_equal(linked_list.get_all_data(), ['bc', 10])

		print('Test: delete general case with no matches')
		linked_list.delete('aa')
		assert_equal(linked_list.get_all_data(), ['bc', 10])

		print('Success: test_delete\n')

	def test_len(self):
		print('Test: len on an empty list')
		linked_list = LinkedList(None)
		assert_equal(len(linked_list), 0)

		print('Test: len general case')
		head = Node(10)
		linked_list = LinkedList(head)
		linked_list.insert_at_start('a')
		linked_list.insert_at_start('bc')
		assert_equal(len(linked_list), 3)

		print('Success: test_len\n')


def main():
	test = TestLinkedList()
	test.test_insert_at_start()
	test.test_append()
	test.test_find()
	test.test_delete()
	test.test_len()


if __name__ == '__main__':
	main()




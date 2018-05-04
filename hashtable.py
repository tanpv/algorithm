"""
	- a hashtable contain 
		- two variables:
			- capacity : refers to the number of buckets in the hash table
			- load : refers to how full the hash table can be before a resize happens
		- two function:
			- set : store key and value to hashtable
			- get : retrieve value from the key

	- handling collision
		- each buckets not store value but a linklist.
		- when ever collision happen, (key,value) is added to linkedlist

	- resizing
		- hashtable need to resize when current item > load
		- rehash all buckets because capacity just changed
"""


def hash(key_str, size):
	return sum([ord(c) for c in key_str]) % size


class HashEntry(object):

	def __init__(self, key, value):
		self.key = key
		self.value = value		
		self.next = None # final item in linkedlist point to None


class HashTable(object):
	
	# init with 2 variables capacity and load
	def __init__(self, capacity, load):
		self.capacity = capacity
		self.load = load
		self.current_capacity = 0
		self.slots = [None] * capacity


	def set(self, key, value):
		key_hashed = hash(key, self.capacity)

		if self.slots[key_hashed] is None:
			self.slots[key_hashed] = HashEntry(key, value)
		else:
			self._add_to_linked_list(key, value, self.slots, key_hashed)


	# check if key is same value
	def _add_to_linked_list(self, key, value, slots, key_hashed):
		# same key found --> update value with new value
		# difference key, and current node is final node in linked list --> add new node to list
		# if current node is not final node --> continue moving on linked list
		current_node = slots[key_hashed]

		while current_node is not None:

			# update value if same key found
			if current_node.key == key:
				print('update happen')
				current_node.value = value
				current_node = None
			else:
				# this is final node
				if current_node.next == None:
					current_node.next = HashEntry(key, value)
				# this is not final node
				# continue to move
				else:
					current_node = current_node.next


	def get(self,key):
		key_hashed = hash(key, self.capacity)
		
		node = self.slots[key_hashed]

		while node is not None:
			if node.key == key:
				return node.value
			else:
				node = node.next


ht = HashTable(1000,500)
ht.set('hello', 4)
print(ht.get('hello'))
ht.set('hello', 5)
print(ht.get('hello'))
ht.set('abc',10)
print(ht.get('abc'))







		









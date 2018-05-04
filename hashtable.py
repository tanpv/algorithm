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


def hash():
	pass

class HashTable(object):
	
	# init with 2 variables capacity and load
	def __init__(self, capacity, load):
		self.capacity = capacity
		self.load = load
		self.current_capacity = 0
		self.slots = [None] * capacity

	def set(self, key, value):
		pass

	def get(self,key):
		pass


class HashEntry(object):
	def __init__(self, key, value):
		self.key = key
		self.value = value
		# final item in linkedlist point to None
		self.next = None

		









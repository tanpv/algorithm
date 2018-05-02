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





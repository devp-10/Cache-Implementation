class ContentItem:
	def __init__(self, cid, size, header, content):
		self.cid = cid
		self.size = size
		self.header = header
		self.content = content

	def __str__(self):
		return ('CONTENT ID: {} SIZE: {} HEADER: {} CONTENT: {}'.format(self.cid, self.size, self.header, self.content))

	__repr__=__str__


class Node:
	def __init__(self, content):
		self.value = content
		self.next = None

	def __str__(self):
		return ('CONTENT:{}\n'.format(self.value))

	__repr__=__str__


class CacheList:
	def __init__(self, size):
		self.head = None
		self.tail = None
		self.maxSize = size
		self.remainingSize = size
		self.numItems = 0

	def __str__(self):
		listString = ""
		current = self.head
		while current is not None:
			listString += "[" + str(current.value) + "]\n"
			current = current.next
		return ('REMAINING SPACE:{}\nITEMS:{}\nLIST:\n{}\n'.format(self.remainingSize, self.numItems, listString))     

	__repr__=__str__

	def __len__(self):
		return self.numItems
	

	def put(self, content, evictionPolicy):
		if self.find(content.cid)!=None:
			return "Insertion of content item {} not allowed. Content already in cache.".format(content.cid)
		elif self.maxSize < content.size:
			return "Insertion not allowed. Content size is too large."
		elif self.maxSize > content.size:
			nn = Node(content)
			while self.remainingSize < content.size:
				if evictionPolicy == "lru":
					self.lruEvict()
				if evictionPolicy == "mru":
					self.mruEvict()

			self.remainingSize -= content.size
			self.numItems += 1
			if self.head == None:
				#nn.next = None
				self.head = nn
				self.tail = nn
			else :
				nn.next = self.head
				self.head = nn
			return "INSERTED: {}".format(content)
		
	
	def find(self, cid):
		current = self.head
		prev=None
		var=None
		while current!=None:
			if current.value.cid==cid:
				var=current.value
				if prev!=None:
					prev.next=current.next
					current.next=self.head
					self.head=current
				break
			else:
				prev=current
				current=current.next
		if var!=None:
			return var
		else:
			return None
		

	def update(self, cid, content):
		finding=self.find(cid)
		if finding!=None:
			finding.content=content
			return "UPDATED: {}".format(finding)
		else:
			return None
		

	def mruEvict(self):
		if self.head == self.tail:
			self.clear()
		else:
			toDelete = self.head.value.size
			self.head = self.head.next
			self.remainingSize += toDelete
			self.numItems -= 1

	
	def lruEvict(self):
		if self.head == self.tail:
			self.clear()
		else:
			current = self.head
			while current.next != self.tail:
				current = current.next
			current.next = None
			toDelete = self.tail.value.size
			self.tail = current
			self.remainingSize += toDelete
			self.numItems -= 1


	def clear(self):
		self.head = None
		self.tail = None
		self.remainingSize = self.maxSize
		self.numItems = 0
		return 'Cleared cache!'



class Cache:
	"""
	A more comprehensive doctest is provided in the doctest.py file. 
	
	>>> cache = Cache()
	>>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
	>>> content2 = ContentItem(1003, 13, "Content-Type: 0", "0xD")
	>>> content3 = ContentItem(1008, 242, "Content-Type: 0", "0xF2")
	>>> cache.insert(content1, 'lru')
	'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
	>>> cache.insert(content2, 'lru')
	'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
	>>> cache.insert(content3, 'lru')
	'Insertion not allowed. Content size is too large.'
	>>> cache
	L1 CACHE:
	REMAINING SPACE:177
	ITEMS:2
	LIST:
	[CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
	[CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
	<BLANKLINE>
	<BLANKLINE>
	L2 CACHE:
	REMAINING SPACE:200
	ITEMS:0
	LIST:
	<BLANKLINE>
	<BLANKLINE>
	L3 CACHE:
	REMAINING SPACE:200
	ITEMS:0
	LIST:
	<BLANKLINE>
	<BLANKLINE>
	<BLANKLINE>
	"""

	def __init__(self):
		self.hierarchy = [CacheList(200) for _ in range(3)]
		self.size = 3
	
	def __str__(self):
		return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))
	
	__repr__=__str__

	def clear(self):
		for item in self.hierarchy:
			item.clear()
		return 'Cache cleared!'

	def hashFunc(self, contentHeader):
		total = 0
		for characters in contentHeader:
			total += ord(characters)
		return (total%self.size)


	def insert(self, content, evictionPolicy):
		level = self.hashFunc(content.header)
		putting = self.hierarchy[level].put(content,evictionPolicy)
		return putting


	def retrieveContent(self, content):
		level = self.hashFunc(content.header)
		retrieving = self.hierarchy[level].find(content.cid)
		if retrieving!=None:
			return content
		else:
			return "Cache miss!"
		

	def updateContent(self, content):
		level = self.hashFunc(content.header)
		upd = self.hierarchy[level].update(content.cid ,content.content)
		if upd!=None:
			return upd
		else:
			return "Cache miss!"

class MyHashSet:
    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        bucket, idx = self._index(key)
        if idx >= 0:
            return
        bucket.append(key)

    def remove(self, key):
        bucket, idx = self._index(key)
        if idx < 0:
            return
        bucket.remove(key)

    def contains(self, key):
        _, idx = self._index(key)
        return idx >= 0

    def _hash(self, key):
        return key % self.size

    def _index(self, key):
        hash = self._hash(key)
        bucket = self.buckets[hash]
        for i, k in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1

class ListNode(object):
    def __init__(self,key,next):
        self.key = key
        self.next = next

class MyHashSet1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [None]*self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketCode = key % self.size
        cur = self.buckets[bucketCode]
        if not cur: 
            self.buckets[bucketCode] = ListNode(key, None)
            return
        if cur.key == key:
            return 
        while cur:
            if cur.key == key: 
                return
            if not cur.next: 
                cur.next = ListNode(key,None)
                return 
            if cur.next: 
                cur = cur.next
        return 

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketCode = key % self.size
        cur = self.buckets[bucketCode]
        if not cur:
            return 
        if cur.key == key:
            self.buckets[bucketCode] = cur.next
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return 
            cur = cur.next
        return
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucketCode = key % self.size
        cur = self.buckets[bucketCode]
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False			
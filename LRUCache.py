import collections
"""This is a very basic implementation. I did not have time to finish everything.
 The schema can be changed to have the following. Instead of one cache we will have many caches based on location. When a new item comes in it will be put in one which is closest geo wise based on geo distance ( (lat1-lat1)^2 + (long1-long2)^2). We will also need to modify the get function to get the closest cache geo wise."""
""" I was also not sure if I could use available libraries. I would have used functools lru_cache. I also found a library called 'pyowm' which is a wrapper around weather api. This has both the lru_cache and geo functionality""" 
class LRUCache():
	def __init__(self, length ):
		self.length = length
                self.cache = collections.OrderedDict()

	def get(self,key):
		try:
			value = self.cache.pop(key)
			self.cache[key] = value
			return value
		except KeyError:
			return -1
        def set(self, key , lat, long, value): 
		try:
			self.cache.pop(key)
		except KeyError:
			if len(self.cache) >= self.length:
				self.cache.popitem(last=False)
		self.cache[key] = [lat,long,value]

one = LRUCache(length=5)

one.set('1', 22.3, 32.3, "first")
one.set('2', 12.3, 44.1, "second")
one.set('3', 23.3, 62.3, "third")
one.set('4', 15.3, 14.1, "fourth")
one.set('5', 24.3, 32.3, "fifth")
one.set('6', 72.3, 84.1, "sixth")
one.set('7', 26.3, 12.3, "seventh")
one.set('8', 15.3, 34.1, "eight")
print one.get('1')
print one.get('2')
print one.get('8')

def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
	up to `maxsize` results based on a Least Recently Used (LRU)
	algorithm.
	"""
	def decorating_function(user_function):
		return _lru_cache(user_function, maxsize=maxsize, typed=typed)

	return decorating_function
def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	def decorating_function(user_function):
		cache = OrderedDict()
		@functools.wraps(user_function)
		def wrapper(*args, **kwargs):
			key = _make_key(args, kwargs, typed)
			if key not in cache:
				cache[key] = user_function(*args, **kwargs)
				if len(cache) > maxsize:
					oldest = cache.pop(list(cache)[0])
					if oldest is not None:
						del oldest
			return cache[key]
		return wrapper
	return decorating_function
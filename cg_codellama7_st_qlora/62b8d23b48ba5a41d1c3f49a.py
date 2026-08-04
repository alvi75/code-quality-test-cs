def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
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
					cache.popitem(last=False)
			return cache[key]
		return wrapper
	return decorating_function
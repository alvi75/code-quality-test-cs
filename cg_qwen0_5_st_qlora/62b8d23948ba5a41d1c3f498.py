def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	def decorator(func):
		cache = {}
		if typed:
			key = lambda x: x.__class__.__name__
		else:
			key = lambda x: str(x)

		def wrapper(*args, **kwargs):
			key_args = [key(arg) for arg in args]
			key_kwargs = [key(arg) for arg in kwargs.items()]
			key_args += list(key_kwargs)
			key_args.sort()
			key_args = tuple(key_args)
			if key_args in cache:
				return cache[key_args]

			result = func(*args, **kwargs)
			if maxsize is not None and len(cache) >= maxsize:
				del cache[cache.keys()[0]]
			cache[key_args] = result
			return result

		return wrapper

	return decorator
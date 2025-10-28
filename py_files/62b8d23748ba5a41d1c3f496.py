def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			key = func.__name__ + str(args) + str(kwargs)
			if key in cache:
				return cache[key]
			else:
				result = func(*args, **kwargs)
				cache[key] = result
				return result
		return wrapper

	return decorator
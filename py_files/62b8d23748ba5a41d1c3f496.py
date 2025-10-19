def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU) algorithm.
	"""
	def decorator(fn):
		cache = LFCache(maxsize=maxsize, typed=typed)

		@functools.wraps(fn)
		def wrapper(*args, **kwargs):
			key = _key(args, kwargs)
			if key not in cache:
				cache[key] = fn(*args, **kwargs)
			return cache[key]
		return wrapper
	return decorator
def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""

	def decorator(f):
		if not _is_hashable(f) or isinstance(f, types.FunctionType):
			raise TypeError('can\'t cache unhashable type: %s' % f)

		cache = dict()
		call_counter = 0

		def wrapper(*args, **kwargs):
			key = args + tuple(sorted(kwargs.items()))
			try:
				result = cache[key]
			except KeyError:
				result = f(*args, **kwargs)
				if maxsize is None or call_counter < maxsize:
					cache[key] = result
					call_counter += 1
			return result

		wrapper.cache_clear = lambda: cache.clear()

		return functools.update_wrapper(wrapper, f)

	return decorator
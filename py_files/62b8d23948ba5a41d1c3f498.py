def _lru_cache(maxsize=128, typed=False):
		""" Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU) algorithm.
	"""
	if typed:
		def inner(f):
			return LRU_TYED_CACHE(maxsize)(f)
	else:
		def inner(f):
			return LRU_CACHE(maxsize)(f)

	return inner
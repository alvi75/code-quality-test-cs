def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""

	def _cachedmethod(func):

		if not hasattr(func, '_cache'):
			func._cache = {}

		def wrapper(*args, **kwargs):
			key = key(args, kwargs)
			try:
				return func._cache[key]
			except KeyError:
				pass

			result = func(*args, **kwargs)

			if lock is None or lock.acquire():
				try:
					func._cache[key] = result
				finally:
					lock.release()

			return result

		return wrapper

	return _cachedmethod
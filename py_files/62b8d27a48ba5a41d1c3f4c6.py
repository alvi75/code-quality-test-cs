def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""

	def _cached(func):

		@wraps(func)
		def wrapper(*args, **kwargs):
			key = key(args, kwargs)

			if not isinstance(key, basestring):
				key = str(key)

			try:
				return cache.get(key)
			except AttributeError:
				pass

			result = func(*args, **kwargs)

			cache.set(key, result)

			return result

		return wrapper

	return _cached
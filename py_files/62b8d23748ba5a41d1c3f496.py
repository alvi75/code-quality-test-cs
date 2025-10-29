def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
	def _decorator(func):
		cache = {}
		def _cache(*args, **kwargs):
			if not hasattr(_cache, 'cache'):
				# Create cache if it doesn't exist
				_cache.cache = {}
			key = str(args) + str(kwargs)
			if key in cache:
				return cache[key]
			else:
				result = func(*args, **kwargs)
				if result is None:
					del cache[key]
				else:
					cache[key] = result
					if len(cache) > maxsize:
						for k in sorted(cache.keys()):
							del cache[k]
				return result

		_cache.__doc__ = func.__doc__
		_cache.__name__ = func.__name__
		_cache.__module__ = func.__module__

		if typed:
			_cache._key_type = type(key)

		return _cache
	return _decorator
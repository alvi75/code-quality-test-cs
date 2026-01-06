def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
	def decorator(f):
		@wraps(f)
		def wrapper(*args, **kwargs):
			key = _get_key(args, kwargs, key)
			if not hasattr(wrapper, '_cache'):
				wrapper._cache = {}
			if key not in wrapper._cache:
				with (lock or Lock()):
					if key not in wrapper._cache:
						result = f(*args, **kwargs)
						cache.set(key, result)
						return result
			else:
				return wrapper._cache[key]
		return wrapper
	return decorator
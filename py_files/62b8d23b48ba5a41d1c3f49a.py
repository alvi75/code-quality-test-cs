def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.
	"""
	if not isinstance(maxsize, int) or maxsize <= 0:
		raise ValueError('maxsize must be an integer > 0')
	if typed and not _is_valid_typekey(typed):
		raise TypeError('expected first argument to be callable')

	def decorating_function(user_function):
		cache = LRUCache(maxsize=maxsize, typed=typed)

		@functools.wraps(user_function)
		def wrapper(*args, **kwargs):
			key = _make_key(user_function, args, kwargs)
			return cache.get(key, user_function(*args, **kwargs))
		return wrapper

	return decorating_function
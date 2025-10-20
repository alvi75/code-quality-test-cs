def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""
	if maxsize is None:
		maxsize = sys.maxsize

	if isinstance(maxsize, int):
		maxsize = LRU(maxsize)
	else:
		raise ValueError('maxsize must be an integer or None')

	def wrapper(func):
		cache = _TTLCache(maxsize=maxsize, ttl=ttl, timer=timer, typed=typed)

		@functools.wraps(func)
		def wrapped(*args, **kwargs):
			key = _make_key(args, kwargs, typed)
			try:
				return cache[key]
			except KeyError:
				result = func(*args, **kwargs)
				cache[key] = result
				return result
			except TypeError:
				# if the function will raise a TypeError when called with the
				# given arguments, return 'None' instead of re-raising the error
				return None
		return wrapped
	return wrapper
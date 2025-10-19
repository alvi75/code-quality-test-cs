def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.
	"""
	if not isinstance(maxsize, int) or maxsize < 0:
		raise ValueError("maxsize must be a positive integer")

	def decorating_function(user_function, *args, **kwargs):
		memoize = _Memoize(mru_lru_cache(maxsize), typed)
		return memoize(user_function, *args, **kwargs)

	return decorating_function
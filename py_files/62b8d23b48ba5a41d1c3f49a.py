def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.
	"""
	def decorator(func):
		cache = {}
		if typed:
			key = lambda x: id(x)
		else:
			key = id

		def wrapper(*args, **kwargs):
			key_args = [key(arg) for arg in args]
			key_kwargs = {key(k): v for k, v in kwargs.items()}
			key_args.extend(key_kwargs.values())
			key_args = tuple(key_args)

			if key_args not in cache:
				cache[key_args] = func(*args, **kwargs)
			return cache[key_args]

		return wrapper

	return decorator
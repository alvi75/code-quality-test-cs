def wrapper(func):
		@functools.wraps(func)
		def wrapped(*args, **kwargs):
			key = hashkey(args, kwargs)
			if key not in cache:
				cache[key] = func(*args, **kwargs)
			return cache[key]
		return wrapped
	cachedmethod.__doc__ = "Decorator for caching results of functions."
	return cachedmethod
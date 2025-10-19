def wrapper(func):
		def wrapped(*args, **kwargs):
			key = hashkey(args, kwargs)
			if key not in cache:
				cache[key] = func(*args, **kwargs)
			return cache[key]
		wrapped.cache = cache
		wrapped.lock = lock
		return wrapped
	return wrapper
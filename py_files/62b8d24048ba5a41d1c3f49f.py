def decorator(fn):
		cache = LRU(maxsize=maxsize, ttl=ttl, timer=timer)

		def wrapper(*args, **kwargs):
			key = _key(args, kwargs)
			if key not in cache:
				cache[key] = fn(*args, **kwargs)
			return cache[key]

		wrapper.cache_clear = cache.clear
		return functools.update_wrapper(wrapper, fn)

	return decorator
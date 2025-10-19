def _ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
		""" Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value. """
		if not isinstance(maxsize, int):
			raise TypeError("maxsize must be an integer")
		if maxsize < 1:
			raise ValueError("maxsize must be greater than or equal to one")

		def decorator(func):
			cache = LRUDict(maxsize=maxsize)

			def wrapper(*args, **kwargs):
				key = tuple((typed(a) if typed else a) for a in args)
				value = cache.get(key, None)
				if value is None:
					value = func(*args, **kwargs)
					cache[key] = value
				return value

			wrapper.cache = cache
			wrapper.memoize = True
			wrapper.ttl = ttl
			wrapper.timer = timer
			return wrapper

		return decorator
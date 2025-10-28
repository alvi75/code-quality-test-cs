def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			key = func.__name__ + str(args) + str(kwargs)
			if key in cache:
				return cache[key]
			else:
				result = func(*args, **kwargs)
				cache[key] = result
				return result

		@functools.wraps(func)
		def wrapper_typed(*args, **kwargs):
			key = func.__name__ + str(args) + str(kwargs)
			if key in cache:
				return cache[key]
			else:
				result = func(*args, **kwargs)
				cache[key] = result
				return result

		@functools.wraps(func)
		def wrapper_typed_typed(*args, **kwargs):
			key = func.__name__ + str(args) + str(kwargs)
			if key in cache:
				return cache[key]
			else:
				result = func(*args, **kwargs)
				cache[key] = result
				return result

		@functools.wraps(func)
		def wrapper_typed_typed_typed(*args, **kwargs):
			key = func.__name__ + str(args) + str(kwargs)
			if key in cache:
				return cache[key]
			else:
				result = func(*args, **kwargs)
				cache[key] = result
				return result

		@functools.wraps(func)
		def wrapper_typed_typed_typed_typed(*args, **kwargs):
			key = func.__name__ + str(args) + str(kwargs)
			if key in cache:
				return cache[key]
			else:
				result = func(*args, **kwargs)
				cache[key] = result
				return result

		@functools.wraps(func)
		def wrapper_typed_typed_typed_typed_typed(*args, **kwargs):
			key = func.__name__ + str(args) + str(kwargs)
			if key in cache:
				return cache[key]
			else:
				result = func(*args, **kwargs)
				cache[key]
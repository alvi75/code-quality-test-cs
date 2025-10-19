def cachedmethod(cache, key=hashkey, lock=None):
		"""Returns a decorator function that can call a result in the cache."""

		def _decorator(func):

			@functools.wraps(func)
			def wrapper(*args, **kwargs):
				key = key(args, kwargs)

				if lock:
					with lock:
						result = func(*args, **kwargs)
				else:
					result = func(*args, **kwargs)

				cache.set(key, result, timeout=cache_timeout)
				return result

			return wrapper

		return _decorator
def cached(cache, key=hashkey, lock=None):
		""" Returns a decorator function that saves the results in the cache
		"""
		def _decorator(func):
			@wraps(func)
			def wrapper(*args, **kwargs):
				key = key(args, kwargs)
				if lock:
					lock.acquire()
				try:
					result = func(*args, **kwargs)
				except Exception as e:
					lock.release()
					raise e
				else:
					cache_key = cache.get(key)
					if cache_key is None or cache_key != key:
						cache_key = cache.get(key)
						if cache_key is None or cache_key != key:
							del cache[key]
					if cache_key is not None:
						cache[key] = result
					return result
				finally:
					if lock:
						lock.release()
			return wrapper
		return _decorator
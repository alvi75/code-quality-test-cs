def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU) algorithm.
	"""
	def _mru_cache(func):
		def _wrapper(*args, **kwargs):
			key = args + tuple(kwargs.items())
			if key not in _MRU_CACHE or maxsize <= 0:
				result = func(*args, **kwargs)
				_MRU_CACHE[key] = result
				return result
			else:
				return _MRU_CACHE.pop(key)
		return _wrapper

	if typed:
		def _mru_cache_typed(func):
			def _wrapper(*args, **kwargs):
				key = args + tuple(kwargs.items())
				if key not in _TYPED_MRU_CACHE or maxsize <= 0:
					result = func(*args, **kwargs)
					_TYPED_MRU_CACHE[key] = result
					return result
				else:
					return _TYPED_MRU_CACHE.pop(key)
			return _wrapper
		return _mru_cache_typed
	return _mru_cache
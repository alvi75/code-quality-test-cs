def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
	def _luf_cache(func):
		def _luf_cache_func(*args, **kwargs):
			key = args + tuple(kwargs.items())
			if key not in _luf_cache._cache:
				result = func(*args, **kwargs)
				if typed:
					assert len(result) == 1, "Expected single value for non-typed call"
					result = result[0]
				_luf_cache._cache[key] = result
			return _luf_cache._cache[key]
		return _luf_cache_func
	return _luf_cache
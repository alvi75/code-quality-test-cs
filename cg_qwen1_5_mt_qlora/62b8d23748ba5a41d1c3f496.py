def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""

	def _lfu_cache(func):

		cache = dict()
		freqs = defaultdict(int)

		def wrapper(*args, **kwargs):
			key = args + tuple(sorted(kwargs.items()))
			if key not in cache:
				cache[key] = func(*args, **kwargs)
				freqs[key] = 0
			else:
				freqs[key] += 1
				cache[key] = cache[key]
			return cache[key]

		wrapper.cache_clear = lambda: freqs.clear()

		@wraps(wrapper)
		def clear():
			for k, v in list(freqs.items()):
				if v > maxsize:
					del cache[k]
					del freqs[k]

		wrapper._clear = clear

		return wrapper

	return _lfu_cache
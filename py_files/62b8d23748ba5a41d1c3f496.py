def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
	def decorating_function(user_function):
		cache = LfuCache(maxsize=maxsize, typed=typed)

		@functools.wraps(user_function)
		def wrapper(*args, **kwargs):
			return cache[args][**kwargs]
		return wrapper
	return decorating_function
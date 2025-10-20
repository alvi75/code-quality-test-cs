def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""

	def decorator(f):

		if not _is_hashable(typed):
			raise TypeError('function %r is not hashable' % f)

		cache = dict()
		lru = OrderedDict()

		def wrapper(*args, **kwargs):
			key = args + tuple(sorted(kwargs.items()))
			hashed_key = hash(key)
			try:
				result = cache[hashed_key]
			except KeyError:
				pass
			else:
				now = timer()
				if now - result[1] <= ttl:
					return result[0]

				del cache[hashed_key]
				del lru[hashed_key]
				del key

			value = f(*args, **kwargs)
			hashed_value = hash(value)
			while len(cache) >= maxsize:
				k, v = lru.popitem(last=False)
				del cache[k]
				del lru[k]
				del k
				del v
				del hashed_value

			cache[hashed_key] = (value, now)
			lru[hashed_key] = hashed_value
			return value

		wrapper.cache_clear = lambda: None
		wrapper.cache_info = lambda: CacheInfo(len(lru), len(cache))
		wrapper.cache_prune = prune_lru
		wrapper.cache_get = get
		wrapper.cache_set = set
		wrapper.cache_del = del_
		wrapper.cache_keys = keys
		wrapper.cache_values = values
		wrapper.cache_items = items
		wrapper.cache_update = update
		wrapper.cache_pop = pop
		wrapper.cache_popitem = popitem
		wrapper.cache_rebuild = rebuild
		wrapper.cache_ttl = ttl
		wrapper.cache_maxsize = maxsize
		wrapper.cache_timer = timer
		wrapper.cache_type = type
		wrapper.cache_hash = hash
		wrapper.cache_hashable = _is_hashable
		wrapper.cache_typed = typed
		wrapper.cache_repr = repr
		wrapper.cache_str = str
		wrapper.cache_format = format
		wrapper.cache_dump = dump
		w
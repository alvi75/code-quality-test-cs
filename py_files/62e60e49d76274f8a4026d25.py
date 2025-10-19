def wrapper(f):
		@functools.wraps(f)
		def wrapped(*args, **kwargs):
			if 'metadata' not in kwargs:
				kw = {
					'metadata': {},
					'timeout': timeout,
				}
				kwargs.update(kw)

			return f(*args, **kwargs)
		return wrapped

	return wrapper
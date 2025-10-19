def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
	def _deprecated(func, *args, **kwargs):
		if not args or not kwargs:
			return func(*args, **kwargs)
		else:
			warning = "Call to deprecated function %s.%s" % (func.__module__, func.__name__)
			warnings.warn_explicit(warning, category=DeprecationWarning, stacklevel=2)
			return func(*args, **kwargs)

	return _deprecated
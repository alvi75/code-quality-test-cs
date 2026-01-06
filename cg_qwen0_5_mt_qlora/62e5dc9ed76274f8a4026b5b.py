def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
	def wrapper(func):
		@functools.wraps(func)
		def wrapped_func(*args, **kwargs):
			if not args or len(args) == 0:
				return func(*args, **kwargs)

			click.echo("Warning: %s is deprecated" % message)
			click.echo("Use %s instead." % func.__name__)
			click.echo("See https://github.com/robertdewitt/python-deprecated#deprecation")
			click.echo("for more information.")
			return func(*args, **kwargs)
		return wrapped_func

	return wrapper
def decorator(func):
		func.__name__ = func.__name__.replace('deprecated', 'DEPRECATED')
		func.__doc__ = "DEPRECATED: %s" % message
		return func

	return decorator
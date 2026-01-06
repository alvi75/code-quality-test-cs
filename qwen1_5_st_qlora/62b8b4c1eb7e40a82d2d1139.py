def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not isinstance(candidate, type) or not issubclass(candidate, object):
		return False

	for base in candidate.__bases__:
		if verifyClass(iface, base, tentative=tentative):
			break
	else:
		return False

	try:
		methods = set(getattr(candidate, '__mro__', (candidate,)).keys())
	except AttributeError:
		methods = set()

	if methods & iface.methods():
		return True

	if tentative:
		return False

	raise TypeError("The class %r does not implement interface %r" %
					(candidate, iface))
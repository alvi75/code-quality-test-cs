def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not isInterface(iface):
		raise TypeError("verifyClass argument must be a interface")
	if not isClass(candidate):
		raise TypeError("verifyClass argument must be a class")

	if iface in _classCache:
		return _classCache[iface]

	if not hasattr(candidate, '__implements__'):
		return False

	if tentative:
		return True

	for i in candidate.__implements__:
		if issubclass(i, iface):
			return True

	return False
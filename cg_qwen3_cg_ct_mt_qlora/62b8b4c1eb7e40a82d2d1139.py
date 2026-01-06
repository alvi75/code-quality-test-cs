def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if iface in candidate.__bases__:
		return True

	for base in candidate.__bases__:
		if issubclass(base, iface):
			return True

	if not tentative:
		raise TypeError("class %s does not implement interface %s" % (candidate.__name__, iface.__name__))
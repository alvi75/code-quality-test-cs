def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not isinstance(candidate, type):
		raise TypeError("candidate must be a class")
	if not isinstance(iface, type):
		raise TypeError("iface must be a class")
	if not issubclass(candidate, iface):
		raise TypeError("candidate must be a subclass of iface")
	if tentative:
		return True
	if not issubclass(iface, object):
		raise TypeError("iface must be a class")
	if not issubclass(candidate, object):
		raise TypeError("candidate must be a class")
	if not issubclass(candidate, iface):
		raise TypeError("candidate must be a subclass of iface")
	return True
def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not isinstance(iface, Interface):
		raise TypeError("iface must be a Interface")
	if not isinstance(candidate, type):
		raise TypeError("candidate must be a type")

	if iface in candidate.__providedBy__:
		return True

	for base in candidate.__bases__:
		if iface in base.__providedBy__:
			return True

	if tentative:
		return False

	for base in candidate.__bases__:
		if not issubclass(base, object):
			continue
		if not hasattr(base, '__implements__'):
			continue
		if iface in base.__implements__:
			return True

	return False
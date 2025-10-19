def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if iface in candidate.__bases__:
		return True

	for base in candidate.__bases__:
		if not verifyClass(iface, base, True):
			return False

	return iface in candidate.__dict__
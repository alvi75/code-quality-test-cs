def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not isinstance(candidate, type):
		raise TypeError("verifyClass() argument 2 must be a class")
	if not isInterface(iface):
		raise TypeError("verifyClass() argument 1 must be an interface")

	if iface in candidate.__providedBy__:
		return

	if tentative:
		candidate.__provides__.append(iface)
	else:
		candidate.__provides__ = [iface] + candidate.__provides__

	for base in candidate.__bases__:
		verifyClass(iface, base, tentative=tentative)
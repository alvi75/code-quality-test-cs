def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not isclass(candidate) or not issubclass(candidate, iface):
		return False

	if tentative:
		return True

	for name in dir(iface):
		if name.startswith('_'):
			continue
		candidate_attr = getattr(candidate, name)
		if not ismethod(candidate_attr) and not isfunction(candidate_attr):
			return False
	return True
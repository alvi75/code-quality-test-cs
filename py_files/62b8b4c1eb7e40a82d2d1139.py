def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if iface in candidate.__mro__:
		return True

	if not hasattr(candidate, '__module__'):
		return False

	if candidate.__module__.startswith('sip') or candidate.__module__ == "__main__":
		return False

	if tentative:
		return True

	return False
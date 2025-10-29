def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if iface not in candidate:
		return False

	if tentative:
		return True

	for attr in ['name', 'description']:
		if attr not in candidate[iface]:
			return False

	return True
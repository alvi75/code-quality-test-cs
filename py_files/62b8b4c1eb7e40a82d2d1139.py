def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if iface not in candidate:
		return False

	if candidate[iface] is None:
		return True

	if candidate[iface].isAbstract():
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() != iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		not candidate[iface].isDerivedFrom(iface):
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate[iface].isDerivedFrom() and \
		candidate[iface].isDerivedFrom() == iface:
		return False

	if candidate
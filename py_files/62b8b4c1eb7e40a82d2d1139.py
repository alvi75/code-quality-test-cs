def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not iface:
		raise ValueError("No interface specified")
	if not candidate:
		raise ValueError("No candidate specified")

	if candidate in iface._classes:
		return True

	if candidate in iface._interfaces:
		return False

	if candidate in iface._methods:
		return False

	if candidate in iface._attributes:
		return False

	if candidate in iface._properties:
		return False

	if candidate in iface._events:
		return False

	if candidate in iface._signals:
		return False

	if candidate in iface._signals.connectable:
		return False

	if candidate in iface._signals.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable.connectable.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable.connectable.connectable.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable.connectable.connectable.connectable.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable.connectable.connectable.connectable.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable.connectable.connectable.connectable.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable.connectable.connectable.connectable.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable.connectable.connectable.connectable.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable.connectable.connectable.connectable.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable.connectable.connectable.connectable.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable.connectable.connectable.connectable.connectable.connectable:
		return False

	if candidate in iface._signals.connectable.connectable.connectable.connectable.connectable.connectable.connectable.connectable:
		return False

	if candidate in iface._signals
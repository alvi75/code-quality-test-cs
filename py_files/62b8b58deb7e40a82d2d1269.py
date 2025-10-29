def directlyProvidedBy(object):
	"""
	Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.
	"""
	interfaces = []
	for interface in object.__class__.directlyProvides:
		if interface not in interfaces:
			interfaces.append(interface)
	return interfaces
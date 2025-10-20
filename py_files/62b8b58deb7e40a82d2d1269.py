def directlyProvidedBy(object):
	"""
	Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.

	"""
	if not hasattr(object, '__implements__'):
		return ()
	interfaces = []
	for interface in getattr(object, '__implements__', ()):
		if isinstance(interface, Interface):
			interfaces.append(interface)
		else:
			interface = getInterface(interface)
			if interface is None:
				continue
			interfaces.append(interface)
	return tuple(interfaces)
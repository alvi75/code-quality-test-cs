def directlyProvidedBy(object):
	"""
	Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.
	"""
	return IDeclaration(
		[interface for interface in getDirectlyProvidedInterfaces(object)
		 if not interface.isVariant()]
	)
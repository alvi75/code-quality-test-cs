def directlyProvidedBy(object):
	"""
	Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.
	"""
	if not hasattr(object, '__providerInterfaces__'):
		return None
	return object.__providerInterfaces__
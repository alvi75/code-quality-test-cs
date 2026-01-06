def directlyProvidedBy(object):
	"""
	Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.
	"""
	if not hasattr(object, '__provided_by__'):
		return None
	return object.__provided_by__
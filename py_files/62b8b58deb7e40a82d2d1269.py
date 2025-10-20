def directlyProvidedBy(object):
	"""
	Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.
	"""
	if not hasattr(object, '__interface__'):
		raise TypeError("object must be an interface")
	return object.__interface__
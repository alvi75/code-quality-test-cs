def directlyProvidedBy(object):
	"""
	Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.
	"""
	if not IProvides.providedBy(object):
		raise TypeError("object is not a zope.interface.interface.IProvides")
	return object.__provides__
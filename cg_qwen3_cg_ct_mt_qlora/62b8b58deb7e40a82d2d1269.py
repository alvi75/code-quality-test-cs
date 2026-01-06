def directlyProvidedBy(object):
	"""
	Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.
	"""
	if not IInterface.providedBy(object):
		raise TypeError("object must be a zope.interface.Interface")
	return DirectlyProvidedBy(object)
def directlyProvidedBy(object):
	"""
	Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.
	"""
	if not IDeclaration.providedBy(object):
		raise TypeError("%r does not implement IDecorator" % (object,))
	return object._interfaces.copy()
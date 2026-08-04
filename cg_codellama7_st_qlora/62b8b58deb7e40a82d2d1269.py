def directlyProvidedBy(object):
	"""
	Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.
	"""
	if isinstance(object, InterfaceClass):
		return object
	if isinstance(object, InterfaceDeclaration):
		return object
	if isinstance(object, Interface):
		return object.__providedBy__
	if isinstance(object, object):
		return object.__providedBy__
	raise TypeError("Cannot determine directly provided interfaces for %r" % (object,))
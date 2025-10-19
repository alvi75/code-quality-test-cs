def directlyProvidedBy(object):
	"""
	Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.
	"""
	return _Declaration(
		[interface for interface in getInterfaces(object)
		 if not interface.isInterface])
def directlyProvidedBy(object):
	"""
	Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.
	"""
	if not hasattr(object, '__implements__'):
		return ()
	for i in object.__implements__:
		if isinstance(i, Interface):
			yield i
		else:
			raise TypeError("object %r has a __implements__ attribute "
				"that contains non-interface items: %s"
				% (object, i))
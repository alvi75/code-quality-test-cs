def directlyProvidedBy(object):
	"""Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.
	"""
	if not hasattr(object, '__implements__'):
		return ()
	interfaces = getattr(object, '__implements__', ())
	for interface in interfaces:
		try:
			yield getDeclaration(interface)
		except TypeError:  # pragma: no cover
			pass
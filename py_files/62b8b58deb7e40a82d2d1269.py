def directlyProvidedBy(object):
	"""
	Return the interfaces directly provided by the given object

The value returned is an `~zope.interface.interfaces.IDeclaration`.
	"""

	ifaces = []
	for iface in object.__metaclass__.__metadict__.get('directlyProvidedBy', []):
		try:
			iface = getattr(iface, 'interface')
		except AttributeError:
			continue
		iface = iface.__class__
		iface = iface.__name__
		iface = iface.lower()
		iface = iface.replace('_', '-')
		iface = iface.replace('-', '_')
		iface = iface.replace('/', '_')
		iface = iface.replace('.', '_')
		iface = iface.replace(',', '_')
		iface = iface.replace(' ', '_')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('[', '')
		iface = iface.replace(']', '')
		iface = iface.replace('{', '')
		iface = iface.replace('}', '')
		iface = iface.replace('!', '')
		iface = iface.replace('?', '')
		iface = iface.replace('"', '')
		iface = iface.replace("'", '')
		iface = iface.replace('\'', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		iface = iface.replace('(', '')
		iface = iface.replace(')', '')
		if
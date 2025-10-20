def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if explicit_mc is not None:
		return explicit_mc

	mc = None
	for base in bases:
		if hasattr(base, '__metaclass__'):
			if mc is None:
				mc = base.__metaclass__
			elif mc != base.__metaclass__:
				raise TypeError('Multiple metaclasses defined for %s: %r and %r' % (base.__name__, mc, base.__metaclass__))
	return mc
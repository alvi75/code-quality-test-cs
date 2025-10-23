def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if explicit_mc is not None:
		return explicit_mc

	mcls = None
	for base in bases:
		if hasattr(base, '__metaclass__'):
			if mcls is not None:
				raise TypeError("Multiple metaclasses specified for %r" % (base,))
			mcls = base.__metaclass__

	return mcls
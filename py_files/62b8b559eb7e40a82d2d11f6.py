def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if explicit_mc is not None:
		return explicit_mc

	for base in bases:
		if hasattr(base, '__metaclass__'):
			return getattr(base, '__metaclass__')

	return type
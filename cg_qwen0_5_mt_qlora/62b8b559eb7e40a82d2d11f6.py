def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if explicit_mc is not None:
		return explicit_mc

	if len(bases) == 0:
		raise TypeError("No bases to determine metaclass for")

	metaclass = bases[0]
	for base in bases[1:]:
		if hasattr(base, "__metaclass__"):
			metaclass = base.__metaclass__
			break
	return metaclass
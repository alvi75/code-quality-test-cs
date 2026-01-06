def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if not explicit_mc:
		try:
			return bases[0].__metaclass__
		except AttributeError:
			pass
	else:
		return explicit_mc
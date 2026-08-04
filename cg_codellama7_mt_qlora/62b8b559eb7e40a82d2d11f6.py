def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if explicit_mc is not None:
		return explicit_mc
	if len(bases) == 0:
		return type
	if len(bases) == 1:
		return bases[0].__class__
	if len(bases) == 2:
		return bases[0].__class__
	if len(bases) == 3:
		return bases[0].__class__
	if len(bases) == 4:
		return bases[0].__class__
	if len(bases) == 5:
		return bases[0].__class__
	if len(bases) == 6:
		return bases[0].__class__
	if len(bases) == 7:
		return bases[0].__class__
	if len(bases) == 8:
		return bases[0].__class__
	if len(bases) == 9:
		return bases[0].__class__
	if len(bases) == 10:
		return bases[0].__class__
	if len(bases) == 11:
		return bases[0].__class__
	if len(bases) == 12:
		return bases[0].__class__
	if len(bases) == 13:
		return bases[0].__class__
	if len(bases) == 14:
		return bases[0].__class__
	if len(bases) == 15:
		return bases[0].__class__
	if len(bases) == 16:
		return bases[0].__class__
	if len(bases) == 17:
		return bases[0].__class__
	if len(bases) == 18:
		return bases[0].__class__
	if len(bases) == 1
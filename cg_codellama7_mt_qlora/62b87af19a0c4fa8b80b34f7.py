def difference(d1, d2, level=-1):
	"""
	Return a dictionary with items from d1 not contained in d2.
	"""
	if level == 0:
		return dict(d1)
	return dict([(k, v) for k, v in d1.items() if k not in d2 or difference(d1[k], d2[k], level-1)])
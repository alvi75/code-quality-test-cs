def difference(d1, d2, level=-1):
	"""
	Return a dictionary with items from d1 not contained in d2.
	"""
	if level < 0:
		return {k: v for k, v in d1.items() if k not in d2}
	else:
		for k, v in d1.items():
			if k in d2:
				difference(d2[k], d1[k], level-1)
			else:
				yield k, v
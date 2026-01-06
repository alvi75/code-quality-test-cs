def difference(d1, d2, level=-1):
	"""
	Return a dictionary with items from d1 not contained in d2.
	"""
	if level == -1:
		level = len(d1)
	if level == 0:
		return {}
	else:
		difference = {}
		for k, v in d1.items():
			if k not in d2 or type(v) != type(d2[k]):
				difference[k] = v
			elif isinstance(v, dict):
				difference[k] = difference(v, d2[k], level-1)
		return difference
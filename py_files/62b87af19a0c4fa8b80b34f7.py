def difference(d1, d2, level=-1):
	"""
	Return a dictionary with items from d1 not contained in d2.
	"""
	difference = {}
	for k,v in d1.items():
		if k not in d2:
			difference[k] = v
		elif isinstance(v, dict) and isinstance(d2[k], dict):
			difference[k] = difference(k, d2[k])
		else:
			if level == -1 or k == level:
				difference[k] = v
	return difference
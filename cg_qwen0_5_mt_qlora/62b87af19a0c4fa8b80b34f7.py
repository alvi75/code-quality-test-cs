def difference(d1, d2, level=-1):
	"""
	Return a dictionary with items from d1 not contained in d2.
	"""
	if isinstance(d1, dict) and isinstance(d2, dict):
		return {k: difference(v, d2, level=level+1) for k, v in d1.items() if k not in d2}
	elif isinstance(d1, list) and isinstance(d2, list):
		return [difference(v, d2, level=level+1) for v in d1]
	else:
		if level == -1:
			return d1
		else:
			return d1[level]
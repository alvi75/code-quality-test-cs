def difference(d1, d2, level=-1):
	"""
	Return a dictionary with items from d1 not contained in d2.
	"""
	if isinstance(d1, dict) and isinstance(d2, dict):
		return {k: v for k, v in d1.items() if k not in d2}
	elif isinstance(d1, list) and isinstance(d2, list):
		return [x for x in d1 if x not in d2]
	else:
		raise TypeError("Can't compare %s and %s" % (type(d1), type(d2)))
def difference(d1, d2, level=-1):
	"""
	Return a dictionary with items from d1 not contained in d2.
	"""
	if level == 0:
		return {}
	elif level < 0:
		dlevel = -level
	else:
		dlevel = None

	result = {}

	for k1, v1 in d1.items():
		if k1 not in d2:
			if isdict(v1) and isdict(d2.get(k1)):
				result[k1] = difference(v1, d2[k1], level=dlevel)
			else:
				result[k1] = v1

	return result
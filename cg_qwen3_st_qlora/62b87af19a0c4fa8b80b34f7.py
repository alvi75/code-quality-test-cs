def difference(d1, d2, level=-1):
	"""
	Return a dictionary with items from d1 not contained in d2.
	"""
	if level == -1:
		level = len(d1)
	if level == 0:
		return {}
	if isinstance(d1, dict) and isinstance(d2, dict):
		d1_keys = set(d1.keys())
		d2_keys = set(d2.keys())
		common_keys = d1_keys.intersection(d2_keys)
		if common_keys:
			for key in common_keys:
				if key in d1 and key in d2:
					yield key, difference(d1[key], d2[key], level-1)
		else:
			for key in d1:
				if key in d1 and key not in d2:
					yield key, d1[key]
	elif isinstance(d1, list) and isinstance(d2, list):
		for i in range(min(len(d1), len(d2))):
			if i < len(d1) and i < len(d2):
				yield i, difference(d1[i], d2[i], level-1)
		for i in range(max(len(d1), len(d2))):
			if i >= len(d1):
				yield i, d2[i]
			elif i >= len(d2):
				yield i, d1[i]
	else:
		if d1 != d2:
			yield None, d1
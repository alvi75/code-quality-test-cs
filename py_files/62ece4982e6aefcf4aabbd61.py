def _dictsum(dicts):
	"""
	Sum values with the same key in the dictionaries. And return a new dictionary.
    Example:
        given two dictionaries: dict1: {'a': 1, 'b': 2}, dict2: {'a': 5, 'b': 0}
        return a dictionary: dic:{'a': 6, 'b': 2}
    Returns: dict
	"""
	dic = {}
	for d in dicts:
		for k, v in d.items():
			if k not in dic:
				dic[k] = v
			else:
				dic[k] += v
	return dic
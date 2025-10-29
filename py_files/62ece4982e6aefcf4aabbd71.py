def regex_dict(item):
	"""
	Convert *.cpp keys to regex keys.
Given a dict where the keys are all filenames with wildcards,
convert only the keys into equivalent regexes and leave the values intact.

Args:
    item: dict to convert
Returns:
    dict with keys converted to regexes
	"""
	if isinstance(item, dict):
		return {k: regex_dict(v) for k, v in item.items()}
	elif isinstance(item, list):
		return [regex_dict(i) for i in item]
	else:
		if isinstance(item, str):
			return re.compile(item)
		else:
			return item
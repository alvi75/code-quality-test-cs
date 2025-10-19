def _dictsum(dicts):
    """
	Sum values with the same key in the dictionaries. And return a new dictionary.
    Example:
        given two dictionaries: dict1: {'a': 1, 'b': 2}, dict2: {'a': 5, 'b': 0}
        return a dictionary: dic:{'a': 6, 'b': 2}
    Returns: dict
	"""
    result = {}
    for k, v in dicts[0].items():
        if k not in result:
            result[k] = v
        else:
            result[k] += v
    for d in dicts[1:]:
        for k, v in d.items():
            if k not in result:
                result[k] = v
            else:
                result[k] += v
    return result
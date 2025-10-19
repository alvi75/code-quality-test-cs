def is_none_string(val: any) -> bool:
	"""
	Check if a string represents a None value.
    Returns:
        Return True if the type of val is string and the lowercase of val is equal to 'none', otherwise return False
	"""
	return isinstance(val, str) and val.lower() == NONE_STRING
def is_none_string(val: any) -> bool:
		"""
		Check if a string represents a None value.
    Returns:
        Return True if the type of val is string and the lowercase of val is equal to 'none', otherwise return False
	"""
	# If the type of val is not string, return False
	if not isinstance(val, str):
		return False

	# If the lowercase of val is equal to 'none', return True
	return val.lower() == "none"
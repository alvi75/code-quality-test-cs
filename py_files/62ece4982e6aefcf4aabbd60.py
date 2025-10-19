def size_to_bytes(size: str) -> int:
	"""
	Convert human readable file size to bytes

    Args:
			size: str, a string representing a human readable file size (eg: '500K')
    Returns:
			int: file size in bytes
	"""
	if not isinstance(size, str):
		raise TypeError("size must be a string")
	if not size:
		raise ValueError("size can't be empty")

	pattern = re.compile(r"(\d+)(\w{1})")
	matches = pattern.findall(size)
	if len(matches) != 1:
		raise ValueError(
			"Invalid size format! Must be <number><letter> where letter is one of K,M,G,T")

	number, unit = matches[0]
	number = int(number)

	if unit == "K":
		return number * 1024
	elif unit == "M":
		return number * 1024 * 1024
	elif unit == "G":
		return number * 1024 * 1024 * 1024
	elif unit == "T":
		return number * 1024 * 1024 * 1024 * 1024
	else:
		raise ValueError(f"Unrecognized unit {unit}")
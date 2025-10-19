def size_to_bytes(size: str) -> int:
	"""
	Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""
	size = size.lower()
	if not size:
		return 0
	elif size[-1] == "k":
		return int(size[:-1]) * 1024
	elif size[-1] == "m":
		return int(size[:-1]) * 1024 * 1024
	elif size[-1] == "g":
		return int(size[:-1]) * 1024 * 1024 * 1024
	else:
		raise ValueError("Invalid file size format")
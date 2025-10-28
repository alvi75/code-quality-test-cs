def size_to_bytes(size: str) -> int:
	"""
	Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""
	if not size:
		return 0
	size = size.strip()
	if not size:
		return 0
	unit = size[-1]
	size = size[:-1]
	if unit == 'M':
		return int(float(size) * 1024)
	elif unit == 'G':
		return int(float(size) * 1024 * 1024)
	else:
		raise ValueError('Invalid size format')
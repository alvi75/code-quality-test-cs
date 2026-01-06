def size_to_bytes(size: str) -> int:
	"""
	Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""

	size = size.lower()
	if not re.match(r'^\d+(?:[kmb]?)?$', size):
		raise ValueError('Invalid file size')

	multiplier = 1
	for char in size[-1]:
		if char == 'k':
			multiplier *= 1024
		elif char == 'm':
			multiplier *= 1024 * 1024
		elif char == 'g':
			multiplier *= 1024 * 1024 * 1024

	return int(float(size[:-1]) * multiplier)
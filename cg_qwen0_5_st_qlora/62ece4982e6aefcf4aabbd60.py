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
	if size.endswith('M'):
		return int(float(size[:-1]) * 1024)
	elif size.endswith('G'):
		return int(float(size[:-1]) * 1024 * 1024)
	else:
		return int(float(size))
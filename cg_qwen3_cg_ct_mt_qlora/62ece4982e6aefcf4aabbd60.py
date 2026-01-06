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

	size = size.upper()
	for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
		if size.endswith(unit):
			return int(float(size[:-len(unit)]) * 1024)
	raise ValueError("Invalid size")
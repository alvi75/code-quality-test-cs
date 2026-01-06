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

	suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
	for suffix in suffixes:
		if size.endswith(suffix):
			return int(float(size[:-len(suffix)]) * 1024)
	else:
		raise ValueError("size must end with one of these suffixes: %s" % ', '.join(suffixes))
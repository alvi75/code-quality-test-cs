def size_to_bytes(size: str) -> int:
	"""
	Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""
	if not isinstance(size, str):
		raise TypeError('size must be of type str')

	size = size.upper()
	prefixes = {'B': 1, 'KB': 1 << 10, 'MB': 1 << 20, 'GB': 1 << 30, 'TB': 1 << 40}
	value = float(size[:-1])
	prefix = size[-1]
	if prefix == ' ':
		return value * prefixes[prefix]
	else:
		return value * prefixes[prefix]
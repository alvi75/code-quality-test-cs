def size_to_bytes(size: str) -> int:
	"""
	Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""
	if not isinstance(size, str):
		return None
	size = re.sub('[a-zA-Z]', '', size)
	m = re.match(r'(\d+)([KMGTP])', size)
	if m is None:
		return None
	size_int = int(m.group(1))
	byte_unit = m.group(2).lower()
	if byte_unit == 'k':
		return size_int * 1024
	elif byte_unit == 'm':
		return size_int * 1024**2
	elif byte_unit == 'g':
		return size_int * 1024**3
	elif byte_unit == 't':
		return size_int * 1024**4
	else:
		return None
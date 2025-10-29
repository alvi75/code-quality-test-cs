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

	sizes = {'B': 1,
			 'KB': 1024,
			 'MB': 1024 * 1024,
			 'GB': 1024 * 1024 * 1024,
			 'TB': 1024 * 1024 * 1024 * 1024}

	try:
		return int(float(size[:-2]) * sizes[size[-2:]])
	except ValueError:
		raise ValueError("Invalid size format")
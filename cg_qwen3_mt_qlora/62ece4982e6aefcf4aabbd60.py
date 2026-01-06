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

	suffix = size[-1].upper()
	if suffix == "B":
		return int(size[:-1])
	elif suffix in ["K", "M", "G"]:
		return int(float(size[:-1]) * 1024 ** ("KM"[suffix.index(suffix)]))
	else:
		raise ValueError("Invalid suffix")
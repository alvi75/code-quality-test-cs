def size_to_bytes(size: str) -> int:
	"""
	Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""
	if not isinstance(size, str):
		raise TypeError('size must be a string')

	suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
	suffix_index = 0
	while suffix_index < len(suffixes) - 1:
		if size.endswith(suffixes[suffix_index]):
			break
		suffix_index += 1
	if suffix_index == 6:
		raise ValueError('File size too large')
	size_num = float(size[:-1])
	return int(size_num * 1024 ** suffix_index)
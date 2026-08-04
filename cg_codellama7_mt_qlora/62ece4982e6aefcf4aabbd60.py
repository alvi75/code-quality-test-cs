def size_to_bytes(size: str) -> int:
    """
    Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""
    if size.endswith('B'):
        size = size[:-1]
    if size.endswith('K'):
        return int(size[:-1]) * 1024
    if size.endswith('M'):
        return int(size[:-1]) * 1024 * 1024
    if size.endswith('G'):
        return int(size[:-1]) * 1024 * 1024 * 1024
    if size.endswith('T'):
        return int(size[:-1]) * 1024 * 1024 * 1024 * 1024
    return int(size)
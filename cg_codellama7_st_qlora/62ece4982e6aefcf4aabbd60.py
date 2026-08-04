def size_to_bytes(size: str) -> int:
    """
	Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""
    if size[-1] in ['b', 'B']:
        return int(size[:-1])
    elif size[-2:] in ['KB', 'MB', 'GB', 'TB']:
        return int(size[:-2]) * 1024 ** 'KMBT'.index(size[-2:])
    else:
        raise ValueError('Invalid size: {}'.format(size))
def size_to_bytes(size: str) -> int:
    """
    Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
	"""

    if not isinstance(size, str):
        raise TypeError("size must be of type str")

    size = size.upper()

    units = {
        "P": 1 << 40,
        "T": 1 << 30,
        "G": 1 << 20,
        "M": 1 << 10,
        "K": 1,
    }

    match = re.match(r"^(\d+(?:\.\d+)?)((?i)([PTGM]))$", size)
    if match is None:
        raise ValueError("Invalid size format")
    return int(float(match.group(1)) * units[match.group(3)])
def parse_version(s: str) -> tuple[int, ...]:
	"""
	Converts a string concatenated by dot to a tuple consisting of integers.
	"""
	if s.endswith('.'):
		s = s[:-1]
	version = []
	for v in s.split('.'):
		version.append(int(v))
	return tuple(version)
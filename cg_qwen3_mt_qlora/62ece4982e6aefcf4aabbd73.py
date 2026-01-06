def split(s, platform='this'):
	"""
	Split the input str under given platform, return the splitting result
    If platform equals 'this', auto-detect current platform.
    If platform equals 1, use POSIX style.
    If platform equals 0, use Windows/CMD style.
    Args:
        s: input str
        platform: 'this' = auto from current platform; 1 = POSIX; 0 = Windows/CMD
    Returns:
        a list of splitting str
	"""
	if platform == 'this':
		platform = sys.platform
	elif platform not in (0, 1):
		raise ValueError('platform must be "this", 0 or 1')
	if platform == 0:
		return re.split(r'[;&|]', s)
	else:
		return re.split(r'[;&|<>\s]+', s)
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
	if platform == 'win32':
		return s.split(';')
	else:
		return s.split(':')
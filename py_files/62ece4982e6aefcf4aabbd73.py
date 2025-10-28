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
		if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
			return s.split(r'\')
		else:
			return s.split('/')
	elif platform == 1:
		return s.split('/')
	elif platform == 0:
		return s.split('\\')
	else:
		raise ValueError("Invalid platform value")
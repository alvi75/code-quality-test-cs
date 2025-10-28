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
		p = platform.system()
	elif platform == 1:
		p = 'posix'
	elif platform == 0:
		p = 'windows'
	else:
		raise Exception('platform must be 1 or 0')
	if p == 'posix':
		return s.split('/')
	elif p == 'windows':
		return s.split('\\')
	else:
		raise Exception('platform must be 1 or 0')
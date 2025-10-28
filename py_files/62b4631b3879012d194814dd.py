def fix_namespace_prefix_w(content):
	"""
	Replace "w:st=" in content with "w-st=".
	"""
	return re.sub(r'(?<=\s)w:(?P<name>[a-z0-9_]+)(?=\=)', lambda m: 'w-%s=' % m.group('name').replace(':', '-'), content)
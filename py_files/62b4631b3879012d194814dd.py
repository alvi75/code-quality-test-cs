def fix_namespace_prefix_w(content):
	"""
	Replace "w:st=" in content with "w-st=".
	"""
	content = re.sub(r'w:\w+:', 'w-st=', content)
	return content
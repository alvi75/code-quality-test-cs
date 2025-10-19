def fix_namespace_prefix_w(content):
	"""
	Replace "w:st=" in content with "w-st=".
	"""
	return re.sub(r'w\:(.*?)=', r'\1-st=', content)
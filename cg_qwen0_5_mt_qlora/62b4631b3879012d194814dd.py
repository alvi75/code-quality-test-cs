def fix_namespace_prefix_w(content):
	"""
	Fix namespace prefix w in content with "w-st=".
	"""
	return re.sub(r'w:(.*)', r'w-st=\1', content)
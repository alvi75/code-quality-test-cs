def fix_namespace_prefix_w(content):
	"""
	Replace "w:st=" in content with "w-st=".
	"""
	return re.sub(r'w:([\w-]+)="([^"]+)"', r'w-st="\1"\2', content)
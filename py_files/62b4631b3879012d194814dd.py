def fix_namespace_prefix_w(content):
	"""
	Replace "w:st=" in content with "w-st=".
	"""
	return re.sub(r'(?<=\b)w:(st|ST)(?=\s)', r'\1', content, flags=re.IGNORECASE)
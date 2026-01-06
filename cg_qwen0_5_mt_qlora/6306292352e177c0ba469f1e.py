def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	text = re.sub(r'\[([^\]]+)\]', r'<a href="\1">\1</a>', text)
	text = re.sub(r'(\w+)', r'<\1>\1</\1>', text)
	return text
def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" class="text-link">\1</a>', text)
	return text
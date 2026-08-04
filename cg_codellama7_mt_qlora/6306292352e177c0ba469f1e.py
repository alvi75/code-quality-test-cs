def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	# Add some attributes to links
	text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2" class="link">\1</a>', text)
	# Linkify textual links
	text = re.sub(r'\[([^\]]+)\]', r'<a href="\1" class="link">\1</a>', text)
	return text
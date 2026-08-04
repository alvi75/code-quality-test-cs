def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	# Add attributes to links
	text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2" class="link">\1</a>', text)
	# Add attributes to images
	text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\.([^\)]+)\)', r'<img src="\2" alt="\1" class="image" />', text)
	# Linkify textual links
	text = re.sub(r'\[([^\]]+)\]', r'<a href="http://\1" class="link">\1</a>', text)
	return text
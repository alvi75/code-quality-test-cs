def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	text = re.sub(r'(\w+:\/\/[^\s]+)', r'<a href="\1">\1</a>', text)
	text = re.sub(r'\b([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})\b', r'<a href="mailto:\1">\1</a>', text)
	return text
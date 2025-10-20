def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	text = re.sub(r'\[([^\]]+)\]\s*', r'<a href="http://www\.([^"]+)" class="link" title="Link to \1">\1</a>', text)
	text = re.sub(r'\[(\w+):(\w+)\]\s*', r'<a href="http://www\.([^"]+)" class="link" title="Link to \1">\2</a>', text)
	text = re.sub(r'(\w+:\w+)\s*', r'<a href="http://www\.([^"]+)" class="link" title="Link to \1">\1</a>', text)
	return text
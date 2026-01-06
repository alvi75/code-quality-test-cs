def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	text = re.sub(r'(?<!\w)(https?://[^\s]+)', r'<a href="\1">\1</a>', text)
	text = re.sub(r'(?<![A-Za-z0-9])@([A-Za-z0-9_]+)', r'<a href="http://twitter.com/\1">@\1', text)
	return text
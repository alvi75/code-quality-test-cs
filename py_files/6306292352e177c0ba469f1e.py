def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	text = re.sub(r'(?<!\S)(https?|ftp)://[^\s/$.?#].[^\s]*', r'<a href="\1://\2">\1://\2</a>', text)
	text = re.sub(r'(?<!\S)(www)[^\s/$.?#].[^\s]*', r'<a href="http://\1.\2">\1.\2</a>', text)
	text = re.sub(r'(?<!\S)(mailto:)[^\s/$.?#].[^\s]*', r'<a href="\1\2">\1\2</a>', text)
	return text
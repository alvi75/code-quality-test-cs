def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	text = re.sub(r'(?<!\S)(?P<url>https?://[^\s]+)', r'<a href="\g<url>" target="_blank">\g<url></a>', text)
	text = re.sub(r'(?<!\S)(?P<url>www\.[^\s]+)', r'<a href="http://\g<url>" target="_blank">http://\g<url></a>', text)
	text = re.sub(r'(?<!\S)(?P<url>[^\s]+@[^\s]+)', r'<a href="mailto:\g<url>" target="_blank">\g<url></a>', text)
	return text
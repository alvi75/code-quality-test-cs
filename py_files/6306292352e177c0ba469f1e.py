def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	text = re.sub(r'((https?|ftp):\/\/.*)(.*)', r'<\1 rel="nofollow" />\2', text)
	text = re.sub(r'(http|ftp)://([\w\d\.]+)', r'<\1 class="url" />\2', text)
	text = re.sub(r'([a-z0-9][a-z0-9\-]*[a-z0-9])', r'<\1 class="url" />\2', text)
	text = re.sub(r'([a-z0-9])([a-z0-9\-]{0,6})', r'<\1 class="url" rel="nofollow" />\2', text)
	text = re.sub(r'([a-z0-9])([a-z0-9\-]{3,})([a-z0-9])', r'<\1 class="url" rel="nofollow" />\2', text)
	text = re.sub(r'([a-z0-9])([a-z0-9\-]{4,})([a-z0-9])', r'<\1 class="url" rel="nofollow" />\2', text)
	text = re.sub(r'([a-z0-9])([a-z0-9\-]{5,})([a-z0-9])', r'<\1 class="url" rel="nofollow" />\2', text)
	text = re.sub(r'([a-z0-9])([a-z0-9\-]{6,})([a-z0-9])', r'<\1 class="url" rel="nofollow" />\2', text)
	text = re.sub(r'([a-z0-9])([a-z0-9\-]{7,})([a-z0-9])', r'<\1 class="url" rel="nofollow" />\2', text)
	text = re.sub(r'([a-z0-9])([a-z0-9\-]{8,})([a-z0-9])', r'<\1 class="url" rel="nofollow" />\2', text)
	text = re.sub(r'([a-z0-9])([a-z0-9\-]{9,})([a-z0-9])', r'<\1 class="url" rel="nofollow" />\2', text)
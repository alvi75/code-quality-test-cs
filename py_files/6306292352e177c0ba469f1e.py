def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	text = text.replace('http://', 'https://')
	text = re.sub(r'(\bwww\.)', '', text)
	text = re.sub(r'\s+', ' ', text)
	text = re.sub(r'\n\s*', '\n', text)
	text = re.sub(r'\n\s', '\n', text)
	text = re.sub(r'\n', ' ', text)
	text = re.sub(r'\s\s+', ' ', text)
	text = re.sub(r'\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s\s\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s\s\s\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s\s\s\s\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s+', ' ', text)
	text = re.sub(r'\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s
def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	if not version:
		return "0.0.1"
	version = re.sub(r'(\d+)(\.\d+)(\.\d+)', r'\3', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\2', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\1', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\2', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\1', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\2', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\1', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\2', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\1', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\2', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\1', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\2', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\1', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\2', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\1', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\2', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\1', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\2', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\1', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\2', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\1', version)
	version = re.sub(r'(\d+)(\.\d+)', r'\2', version)
	version = re.sub(r'(\d+)(\.\d+
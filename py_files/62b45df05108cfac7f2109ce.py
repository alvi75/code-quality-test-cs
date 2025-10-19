def validate(self, path):
	'''
	Returns True if OCFL object at path or pyfs root, False otherwise.
	'''
	if self.is_root(path) or not os.path.exists(path):
		return True

	f = open(os.path.join(path, '.ocfl'), 'r')
	try:
		data = json.load(f)
	except ValueError as e:
		self.logger.error('Error parsing ocfl file: %s', str(e))
		return False
	finally:
		f.close()

	if data['type'] != 'ocfl':
		return False

	if data.get('version') != VERSION:
		self.logger.error('Invalid version in ocfl file: %s', data['version'])
		return False

	if data.get('name') == '':
		self.logger.error('Empty name in ocfl file: %s', data['name'])
		return False

	if data.get('url') == '':
		self.logger.error('Empty url in ocfl file: %s', data['url'])
		return False

	if data.get('description') == '':
		self.logger.error('Empty description in ocfl file: %s', data['description'])
		return False

	if data.get('license') == '':
		self.logger.error('Empty license in ocfl file: %s', data['license'])
		return False

	return True
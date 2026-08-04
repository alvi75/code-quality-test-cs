def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	if not self.storage_root.exists():
		self.storage_root.mkdir()
		self.storage_root.joinpath('config.json').write_text(json.dumps(self.config))
		self.storage_root.joinpath('inventory.json').write_text(json.dumps(self.inventory))
		self.storage_root.joinpath('log.txt').write_text('')
		self.storage_root.joinpath('log.txt').chmod(0o666)
		self.storage_root.joinpath('log.txt').chown(self.config['user'], self.config['group'])
		self.storage_root.joinpath('log.txt').chgrp(self.config['group'])
		self.storage_root.joinpath('log.txt').touch()
		self.storage_root.joinpath('log.txt').chmod(0o666)
		self.storage_root.joinpath('log.txt').chown(self.config['user'], self.config['group'])
		self.storage_root.joinpath('log.txt').chgrp(self.config['group'])
		self.storage_root.joinpath('log.txt').touch()
		self.storage_root.joinpath('log.txt').chmod(0o666)
		self.storage_root.joinpath('log.txt').chown(self.config['user'], self.config['group'])
		self.storage_root.joinpath('log.txt').chgrp(self.config['group'])
		self.storage_root.joinpath('log.txt').touch()
		self.storage_root.joinpath('log.txt').chmod(0o666)
		self.storage_root.joinpath('log.txt').chown(self.config['user'], self.config['group'])
		self.storage_root.joinpath('log.txt').chgrp(self.config['group
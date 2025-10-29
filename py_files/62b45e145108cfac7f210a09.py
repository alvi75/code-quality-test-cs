def check_digests_present_and_used(self, manifest_files, digests_used):
	"""
	Check all digests in manifest that are needed are present and used. Return error() in the class.
	"""
	for file_name in manifest_files:
		if not os.path.exists(file_name):
			self.error("File %s does not exist." % file_name)
		else:
			digest = self.get_digest(file_name)
			if digest is None:
				self.error("Digest for %s not found." % file_name)
			elif digest not in digests_used:
				self.error("Digest for %s not used." % file_name)
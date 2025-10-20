def check_digests_present_and_used(self, manifest_files, digests_used):
	"""
	Check all digests in manifest that are needed are present and used. Return error() in the class.
	"""
	for file_name in manifest_files:
		if not self.check_file_exists(file_name):
			self.error("File %s does not exist." % file_name)
		else:
			if file_name not in digests_used:
				self.error("Digest for file %s is missing." % file_name)
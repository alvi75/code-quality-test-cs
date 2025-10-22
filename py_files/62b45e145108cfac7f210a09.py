def check_digests_present_and_used(self, manifest_files, digests_used):
	"""
	Check all digests in manifest that are needed are present and used. Return error() in the class.
	"""
	for digest in digests_used:
		if not digest in manifest_files:
			self.error("Digest %s is not present in manifest" % digest)
def check_digests_present_and_used(self, manifest_files, digests_used):
	"""
	Check all digests in manifest that are needed are present and used. Return error() in the class.
	"""
	for digest in digests_used:
		if not self.check_digest_in_manifest(digest, manifest_files):
			return False
	return True
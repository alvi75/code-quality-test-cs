def check_digests_present_and_used(self, manifest_files, digests_used):
		"""
		Check all digests in manifest that are needed are present and used. Return error() in the class.
		"""
		digests_needed = set(digests_used.keys()) - set(manifest_files)
		if len(digests_needed) > 0:
			self.error("The following digests were not found in the manifest: %s" % ', '.join(digests_needed))
		digests_missing = set(manifest_files) - set(digests_used.values())
		if len(digests_missing) > 0:
			self.error("The following digests were expected but were not found: %s" % ', '.join(digests_missing))
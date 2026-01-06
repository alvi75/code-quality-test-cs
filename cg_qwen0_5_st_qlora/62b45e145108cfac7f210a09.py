def check_digests_present_and_used(self, manifest_files, digests_used):
	"""
	Check all digests in manifest that are needed are present and used. Return error() in the class.
	"""
	for file_name in manifest_files:
		if not self.check_file_exists(file_name):
			return "File %s does not exist" % file_name
		if not self.check_file_is_a_file(file_name):
			return "File %s is not a file" % file_name
		if not self.check_file_is_not_a_directory(file_name):
			return "File %s is a directory" % file_name
		if not self.check_file_has_content(file_name):
			return "File %s has no content" % file_name
		if not self.check_file_has_hash(file_name):
			return "File %s does not have a hash" % file_name
		if not self.check_file_has_hashed_content(file_name):
			return "File %s has no hashed content" % file_name
		if not self.check_file_has_hashed_content(file_name):
			return "File %s has no hashed content" % file_name
		if not self.check_file_has_hashed_content(file_name):
			return "File %s has no hashed content" % file_name
		if not self.check_file_has_hashed_content(file_name):
			return "File %s has no hashed content" % file_name
		if not self.check_file_has_hashed_content(file_name):
			return "File %s has no hashed content" % file_name
		if not self.check_file_has_hashed_content(file_name):
			return "File %s has no hashed content" % file_name
		if not self.check_file_has_hashed_content(file_name):
			return "File %s has no hashed content" % file_name
		if not self.check_file_has_hashed_content(file_name):
			return "File %s has no hashed content" % file_name
		if not self.check_file_has_hashed_content(file_name):
			return "File %s has no hashed content" % file_name
		if not self.check_file_has_hashed_content(file_name):
			return "File %s has no hashed content" % file_name
		if not self.check_file_has_hashed_content(file_name):
			return "File %s has no hashed content" % file_name
		if not self.check_file_has_hashed_content(file_name):
			return "File %s has no hashed content" % file
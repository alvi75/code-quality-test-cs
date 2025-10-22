def get_repo_archive(url: str, destination_path: Path) -> Path:
	"""
	Given an url and a destination path, retrieve and extract .tar.gz archive which contains 'desc' file for each package

        Args:
            url: url of the .tar.gz archive to download
            destination_path: the path on disk where to extract archive
        Returns:
                path where the archive is extracted to
	"""
	if not os.path.exists(destination_path):
		os.makedirs(destination_path)
	tar = tarfile.open(fileobj=urlopen(url), mode='r|gz')
	for member in tar.getmembers():
		member_path = destination_path / member.name
		if member.isdir():
			os.makedirs(member_path)
		else:
			with open(member_path, 'wb') as f:
				f.write(tar.extractfile(member).read())
	return destination_path
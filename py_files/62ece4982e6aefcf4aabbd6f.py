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
	with requests.get(url, stream=True) as r:
		r.raise_for_status()
	with tarfile.open(fileobj=r.raw_fileobj, mode='r') as tar:
		for member in tar.getmembers():
			if member.name.endswith('.desc'):
				tar.extract(member, destination_path)
	return destination_path
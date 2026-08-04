def get_repo_archive(url: str, destination_path: Path) -> Path:
	"""
	Given an url and a destination path, retrieve and extract .tar.gz archive which contains 'desc' file for each package

        Args:
            url: url of the .tar.gz archive to download
            destination_path: the path on disk where to extract archive
        Returns:
                path where the archive is extracted to
	"""
	if not destination_path.exists():
		destination_path.mkdir(parents=True)
	archive_path = destination_path / 'repo.tar.gz'
	if not archive_path.exists():
		print('Downloading repo archive from {}'.format(url))
		with urllib.request.urlopen(url) as response, open(archive_path, 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
	print('Extracting repo archive to {}'.format(destination_path))
	with tarfile.open(archive_path, 'r:gz') as tar:
		tar.extractall(destination_path)
	return destination_path
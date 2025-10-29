def get_repo_archive(url: str, destination_path: Path) -> Path:
	"""
	Given an url and a destination path, retrieve and extract .tar.gz archive which contains 'desc' file for each package

        Args:
            url: url of the .tar.gz archive to download
            destination_path: the path on disk where to extract archive
        Returns:
                path where the archive is extracted to
	"""
	archive = requests.get(url)
	with open(archive.url, "wb") as f:
		f.write(archive.content)

	# Extract tar.gz archive
	with tarfile.open(archive.name, "r:gz") as t:
		t.extractall(path=destination_path)

	return destination_path
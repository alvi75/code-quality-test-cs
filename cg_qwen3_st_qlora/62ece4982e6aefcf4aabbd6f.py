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
	archive_path = destination_path / "repo.tar.gz"
	if not os.path.exists(archive_path):
		logger.info("Downloading repo archive from %s", url)
		with open(archive_path, "wb") as f:
			f.write(requests.get(url).content)

	logger.info("Extracting repo archive to %s", destination_path)
	tar = tarfile.open(str(archive_path))
	tar.extractall(path=str(destination_path))
	return destination_path
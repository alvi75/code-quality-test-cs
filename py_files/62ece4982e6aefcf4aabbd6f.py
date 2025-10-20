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
	# TODO: add support for other formats
	archive = destination_path / "packages.tar.gz"
	if not archive.exists():
		logger.info("Downloading %s", url)
		response = requests.get(url)
		with open(archive, "wb") as f:
			f.write(response.content)

	logger.info("Extracting packages")
	tar = tarfile.open(str(archive))
	tar.extractall(path=str(destination_path))
	return destination_path
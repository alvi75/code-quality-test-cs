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

	filename = os.path.basename(url)
	download_url(url=url, filename=filename, destination_path=destination_path)

	tar = tarfile.open(os.path.join(destination_path, filename), "r:gz")
	tar.extractall(path=str(destination_path))
	tar.close()
	return destination_path
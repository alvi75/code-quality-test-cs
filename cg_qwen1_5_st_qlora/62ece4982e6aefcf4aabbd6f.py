def get_repo_archive(url: str, destination_path: Path) -> Path:
	"""
	Given an url and a destination path, retrieve and extract .tar.gz archive which contains 'desc' file for each package

        Args:
            url: url of the .tar.gz archive to download
            destination_path: the path on disk where to extract archive
        Returns:
                path where the archive is extracted to
	"""

	if not url.endswith('.tar.gz'):
		raise ValueError('Only tar.gz archives supported')

	destination_path = Path(destination_path)
	destination_path.mkdir(parents=True, exist_ok=True)

	filename = url.split('/')[-1]
	filepath = destination_path / filename
	logger.info(f'Downloading {url} to {filepath}')

	response = requests.get(url, stream=True)
	response.raise_for_status()

	with open(filepath, 'wb') as f:
		for chunk in response.iter_content(chunk_size=8192):
			f.write(chunk)

	return filepath
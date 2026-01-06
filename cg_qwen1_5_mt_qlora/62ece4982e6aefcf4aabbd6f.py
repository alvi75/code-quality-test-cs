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

	response = requests.get(url)
	with open(destination_path / "repo.tar.gz", "wb") as f:
		f.write(response.content)

	tar = tarfile.open(str(destination_path / "repo.tar.gz"))
	for member in tar.getmembers():
		if member.name.endswith("desc"):
			desc_file = tar.extract(member, destination_path)
			break
	else:
		raise ValueError(f"Could not find desc file in {url}")

	return destination_path / "repo.tar.gz"
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
		os.makedirs(destination_path)

	with tarfile.open(io.BytesIO(urlopen(url).read())) as t:
		for member in t.getmembers():

			if member.name.endswith('.zip'):
				filepath = os.path.join(destination_path, member.name)
				t.extract(member, filepath)
				yield filepath
def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
	"""
	Given an existing archive_path, uncompress it.
    Returns a file repo url which can be used as origin url.

    This does not deal with the case where the archive passed along does not exist.
    @param archive_path : archive file path
    @param filename: File name
    @param tmp_path: Temporary file path
    @return Repo URL
	"""
	if isinstance(archive_path, Path):
		archive_path = archive_path.resolve()
	if not archive_path.exists():
		raise FileNotFoundError(f"File {archive_path} doesn't exist")
	if filename is None:
		filename = archive_path.stem

	tmpdir = PosixPath(tmp_path)
	tmpdir.mkdir()

	with tarfile.TarFile(fileobj=io.BytesIO(archive_path.read_bytes()), mode="r") as tf:
		for member in tf.getmembers():
			if member.name == filename:
				filepath = tf.extractfile(member)
				break
	else:
		raise ValueError("No file named " f"{filename} found in archive")

	return f"https://github.com/{tmpdir}/blob/master/{filepath}"
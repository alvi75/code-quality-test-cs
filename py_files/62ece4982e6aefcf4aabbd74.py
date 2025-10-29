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
	if not os.path.exists(archive_path):
		raise ValueError("Archive path does not exist")
	if not os.path.isfile(archive_path):
		raise ValueError("Archive path is not a file")

	tmp_dir = PosixPath(tmp_path)
	tmp_dir.mkdir(parents=True)

	with tarfile.open(archive_path, "r") as tar:
		tar.extractall(path=tmp_dir)
		tar.close()

	return f"git+{tmp_dir / filename}"
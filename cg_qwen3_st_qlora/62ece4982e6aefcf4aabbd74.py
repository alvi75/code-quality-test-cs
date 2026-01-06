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
	if filename is None:
		filename = os.path.basename(archive_path)
	tmp_dir = PosixPath(tmp_path)
	tmp_repo_path = tmp_dir / filename
	if not tmp_repo_path.exists():
		with open(archive_path, "rb") as f:
			with tarfile.open(fileobj=f, mode="r|gz") as t:
				t.extractall(path=tmp_dir)
	return str(tmp_repo_path.resolve())
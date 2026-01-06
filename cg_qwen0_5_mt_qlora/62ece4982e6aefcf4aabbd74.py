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
		raise ValueError("Archive does not exist")
	if not filename:
		filename = os.path.basename(archive_path)
	archive_path = os.path.join(tmp_path, filename)

	with open(archive_path, "rb") as f:
		archive = tarfile.open(fileobj=f, mode="r:bz2")

	repo_url = archive.extractfile(filename).name
	return repo_url
def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
):
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
		raise ValueError("Archive %s does not exist" % archive_path)
	tmp_dir = Path(tmp_path).expanduser().resolve()
	if not tmp_dir.is_dir():
		os.makedirs(str(tmp_dir))
	archive_name = os.path.basename(filename or archive_path)
	# Unzip to temporary directory
	with zipfile.ZipFile(archive_path, 'r') as zip_ref:
		zip_ref.extractall(str(tmp_dir))

	# Find the first file in the archive
	for root, dirs, files in os.walk(str(tmp_dir)):
		for f in files:
			file_path = os.path.join(root, f)
			break

	# Create repo from extracted file
	repo_url = create_repo_from_file(file_path)

	# Clean up
	shutil.rmtree(str(tmp_dir), ignore_errors=True)
	return repo_url
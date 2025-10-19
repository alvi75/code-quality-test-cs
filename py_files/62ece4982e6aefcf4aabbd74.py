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
	tmp_dir = posixpath.join(tmp_path, "unzip")
	try:
		os.makedirs(tmp_dir)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise

	if archive_path.endswith(".bz2"):
		unarchive_bz2(archive_path, tmp_dir)
	elif archive_path.endswith(".gz"):
		unarchive_gz(archive_path, tmp_dir)
	else:
		unarchive_tar(archive_path, tmp_dir)

	files = glob.glob(posixpath.join(tmp_dir, "*"))
	assert len(files) == 1, "Expecting exactly one file in %s" % (tmp_dir,)
	file_path = files[0]
	return "file://%s/%s" % (posixpath.abspath(tmp_dir), posixpath.relpath(file_path, tmp_dir))
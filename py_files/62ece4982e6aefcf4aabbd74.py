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
        raise Exception("Archive {} does not exist".format(archive_path))

    # Get the filename from the archive_path
    if filename is None:
        filename = os.path.basename(archive_path)

    # Unzip the archive to a temporary directory
    temp_dir = tempfile.mkdtemp(dir=tmp_path)
    try:
        with zipfile.ZipFile(archive_path) as zip_file:
            zip_file.extractall(temp_dir)
    except zipfile.error as e:
        raise Exception("Error extracting archive {}".format(archive_path)) from e

    # Return the repo url for the extracted files
    return "file:///{}".format(os.path.abspath(temp_dir))
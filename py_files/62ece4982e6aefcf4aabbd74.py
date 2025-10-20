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
        raise ValueError("Archive Path {} does not exist".format(archive_path))

    # Get the filename from the archive_path
    if filename is None:
        filename = os.path.basename(archive_path)

    # Create temporary directory to extract the archive into
    tmp_dir = PosixPath(tmp_path).joinpath(filename)
    try:
        os.makedirs(str(tmp_dir))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    # Extract the archive into the temp dir
    logger.info("Extracting archive %s", archive_path)
    with tarfile.open(archive_path, "r") as tar:
        tar.extractall(path=str(tmp_dir))

    # Find the repository in the extracted files
    for root, dirs, files in os.walk(str(tmp_dir)):
        for f in files:
            if f.endswith(".git"):
                repo_url = os.path.join(root, f)
                break
        else:
            continue
        break
    else:
        raise ValueError("Could not find git repository")

    return repo_url
def _extract_tar_gz(archive_url: str, dest_path: Path):
		"""Extracts tar.gz archive from url into dest_path"""
		with urllib.request.urlopen(archive_url) as f:
			with open(dest_path, "wb") as out_f:
				out_f.write(f.read())
		return dest_path


	# Download archive
	download_url = url + "/download"
	download_file_name = os.path.basename(download_url)
	download_file_path = destination_path / download_file_name
	download_file_size = os.path.getsize(download_file_path)

	if not download_file_path.exists():
		download_file_size = 0
	elif download_file_size == 0:
		raise ValueError("Downloaded file size is zero")

	download_file_size_mb = download_file_size / 1e6
	download_file_size_gb = download_file_size / 1e9

	print("Downloading {} bytes ({} MB/{} GB)...".format(
		download_file_size,
		download_file_size_mb,
		download_file_size_gb))

	download_file = _download_to_cache_if_needed(download_file_name, download_file_size_mb, download_file_size_gb)

	# Extract archive
	extract_file = _extract_tar_gz(download_file, destination_path)

	return extract_file
def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""
	image_id = None
	netloc = None
	use_ssl = False

	if not image_href.startswith("http"):
		raise ValueError("Invalid image href")

	image_id = image_href[7:]

	if image_href.endswith("/"):
		image_id += "/"

	if image_href.endswith(".tar.gz"):
		image_id += ".tgz"

	if image_href.endswith(".tar.bz2"):
		image_id += ".tbz"

	if image_href.endswith(".tar.xz"):
		image_id += ".txz"

	if image_href.endswith(".tar"):
		image_id += ".tar"

	if image_href.endswith(".tar.bz2"):
		image_id += ".bz2"

	if image_href.endswith(".tar.gz"):
		image_id += ".gz"

	if image_href.endswith(".tar.xz"):
		image_id += ".xz"

	if image_href.endswith(".tar"):
		image_id += ".tar"

	if image_href.endswith(".tar.bz2"):
		image_id += ".bz2"

	if image_href.endswith(".tar.gz"):
		image_id += ".gz"

	if image_href.endswith(".tar.xz"):
		image_id += ".xz"

	if image_href.endswith(".tar"):
		image_id += ".tar"

	if image_href.endswith(".tar.bz2"):
		image_id += ".bz2"

	if image_href.endswith(".tar.gz"):
		image_id += ".gz"

	if image_href.endswith(".tar.xz"):
		image_id += ".xz"

	if image_href.endswith(".tar"):
		image_id += ".tar"

	if image_href.endswith(".tar.bz2"):
		image_id += ".bz2"

	if image_href.endswith(".tar.gz"):
		image_id += ".gz"

	if image_href.endswith(".tar.xz"):
		image_id += ".xz"

	if image_href.endswith(".tar"):
		image_id += ".tar"

	if image_href.endswith(".tar.bz2"):
		image_id += ".bz2"

	if image_href.endswith(".tar.gz"):
		image_id += ".gz"

	if image_href.endswith(".tar.xz"):
		image_id += ".xz"

	if image_href.endswith(".tar"):
		image_id += ".tar"

	if image_href.endswith(".tar.bz2"):
		image_id += ".bz2"

	if image
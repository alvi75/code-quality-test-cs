def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""

	if not isinstance(image_href, six.string_types):
		raise TypeError("Expected string for image_href")

	image_id = None
	netloc = None
	use_ssl = False

	parsed_url = urlparse(image_href)

	if parsed_url.scheme == "https":
		use_ssl = True

	if parsed_url.netloc is not None:
		netloc = parsed_url.netloc

	if parsed_url.path.startswith("/"):
		image_id = parsed_url.path[1:]

	return image_id, netloc, use_ssl
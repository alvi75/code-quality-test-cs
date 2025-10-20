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

	if not image_href.startswith('http'):
		raise ValueError("Image href must start with http or https")

	parts = urlparse.urlsplit(image_href)

	if parts.scheme == 'https':
		use_ssl = True

	if parts.netloc is not None:
		netloc = parts.netloc

	if parts.path is not None:
		image_id = parts.path[1:]

	return image_id, netloc, use_ssl
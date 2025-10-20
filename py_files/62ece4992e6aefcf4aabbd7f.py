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
		raise ValueError("Invalid image href: %s" % image_href)

	image_id_match = re.match(r'([^/]+)(?:/[^\s]+)?$', image_href)
	if image_id_match is None:
		raise ValueError("Invalid image href: %s" % image_href)

	image_id = image_id_match.group(1)
	netloc = image_id_match.group(2)

	if image_id == 'default':
		image_id = None
		use_ssl = True

	return image_id, netloc, use_ssl
def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""
	if not isinstance(image_href, str):
		raise TypeError("image_href must be a string")
	match = re.match(r"^(?P<image_id>.*)://(?P<netloc>.+)$", image_href)
	if match is None:
		raise ValueError(
			"Invalid image reference '%s'. Must be in <image_id>://<netloc> format." % (
				image_href))
	image_id = match.groupdict()['image_id']
	netloc = match.groupdict()['netloc']
	use_ssl = netloc.startswith('https')
	return image_id, netloc, use_ssl
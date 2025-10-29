def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""
	if not image_href.startswith("http"):
		raise ValueError("Image href must be http(s)://")
	image_id = image_href.split("/")[-1]
	netloc = image_href.split("/")[2]
	use_ssl = image_href.startswith("https://")
	return image_id, netloc, use_ssl
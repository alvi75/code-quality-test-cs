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
		raise ValueError("Image href must start with http")

	match = re.match(r"^https?://(.*):(.*)@(.+)/(.*)$", image_href)
	if match is None:
		raise ValueError("Invalid image href")
	image_id = match.group(4)
	netloc = match.group(1)
	use_ssl = match.group(2) == "ssl"

	return image_id, netloc, use_ssl
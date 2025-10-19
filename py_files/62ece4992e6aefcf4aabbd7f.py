def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""
	image_id = None
	ssl = False
	if "://" in image_href:
		netloc, path, query, fragment = urlparse(image_href)
		if not netloc or netloc == "":
			raise ValueError("Invalid image url: {}".format(image_href))
		if query is not None and query != "":
			raise ValueError("Invalid image url: {}".format(image_href))
		if fragment is not None and fragment != "":
			raise ValueError("Invalid image url: {}".format(image_href))
		if netloc.startswith("http"):
			pass
		elif netloc.startswith("https"):
			ssl = True
		else:
			raise ValueError("Invalid image url: {}".format(image_href))
		image_id = path.split("/")[-1]
	return image_id, netloc, ssl
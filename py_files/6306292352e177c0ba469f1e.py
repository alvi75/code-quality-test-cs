def process_text_links(text):
	"""
	Process links in text, adding some attributes and linkifying textual links.
	"""
	def _sub(match):
		match = match.group(0)
		if not match.startswith("<"):
			return match

		link = match[1:-1]
		if "://" not in link:
			return match

		link_attrs = {}
		link_text = link
		linkify = True

		if link.endswith("/"):
			link = link[:-1]

		if link.startswith("#"):
			link = "http://"+request.host+link

		if link.startswith("http://") or link.startswith("https://"):
			linkify = False
			link = link[7:]
			link_attrs["href"] = link
		elif link.startswith("//"):
			link_attrs["href"] = "http:" + link
			link = link[2:]
		elif link.startswith("/"):
			link = request.host_url + link
			link_attrs["href"] = link
		else:
			link = request.host_url + "/" + link
			link_attrs["href"] = link

		if link.endswith("/") and not link.endswith("/<"):
			link_text = link[:-1]

		if "<" in link_text:
			link_text = markupsafe.Markup(link_text)

		if linkify:
			link_attrs["class"] = "external"
			link_attrs["target"] = "_blank"

		return '<a href="{href}" class="{class_}" target="{target}">{text}</a>'.format(**link_attrs)

	return re.sub(r"<([^>]*)>", _sub, text)
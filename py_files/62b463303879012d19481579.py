def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Return the possible values of number and sup from the contents of issue.
	"""
	number = None
	sup = None

	if issue is not None:
		for child in issue.childNodes:
			if child.nodeType == Node.TEXT_NODE:
				number = child.data
			elif child.nodeName == 'sup':
				sup = child.firstChild.data

	return number, sup
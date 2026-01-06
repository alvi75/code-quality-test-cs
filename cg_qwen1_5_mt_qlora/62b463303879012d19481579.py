def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Return the possible values of number and sup from the contents of issue.
	"""
	number = None
	supplement = None

	for child in issue:
		if child.tag == 'number':
			number = child.text
		elif child.tag == 'sup':
			supplement = child.text

	return (number, supplement)
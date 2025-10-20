def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Return the possible values of number and sup from the contents of issue.
	"""
	number = None
	sup = None

	if issue is not None:
		number = issue.get_text_content()
		sup = issue.find('sup')

	return number, sup
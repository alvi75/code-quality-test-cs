def _extract_number_and_supplement_from_issue_element(issue):
	"""
	Return the possible values of number and sup from the contents of issue.
	"""
	number = None
	supplement = None

	if 'number' in issue:
		number = issue['number']
	elif 'supplement' in issue:
		supplement = issue['supplement']

	return number, supplement
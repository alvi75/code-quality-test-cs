def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Return the possible values of number and sup from the contents of issue.
	"""
	number = None
	sup = None

	if 'number' in issue:
		number = issue['number']
	elif 'id' in issue:
		number = issue['id']

	if 'supplemental' in issue:
		sup = issue['supplemental']

	return (number, sup)
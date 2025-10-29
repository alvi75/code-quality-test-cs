def _extract_number_and_supplement_from_issue_element(issue):
	"""
	Return the possible values of number and sup from the contents of issue.
	"""
	number = issue.get('number')
	sup = issue.get('supplementaryMaterial', {}).get('supplementaryMaterialType', None)
	return number, sup
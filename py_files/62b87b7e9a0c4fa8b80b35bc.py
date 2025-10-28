def _update_context(self, context):
	"""
	Update *context* with the properties of this graph.

*context.error* is appended with indices of errors.
Example subcontext for a graph with fields "E,t,error_E_low":
{"error": {"x_low": {"index": 2}}}.
Note that error names are called "x", "y" and "z"
(this corresponds to first three coordinates,
if they are present), which allows to simplify plotting.
Existing values are not removed
from *context.value* and its subcontexts.

Called on "destruction" of the graph (for example,
in :class:`.ToCSV`). By destruction we mean conversion
to another structure (like text) in the flow.
The graph object is not really destroyed in this process.
	"""
	if self._errors:
		context.error = {k: v.index() for k,v in self._errors.items()}
	for field in self.fields:
		if isinstance(field, FieldError):
			continue
		if field.name == 'error':
			continue
		value = getattr(self, field.name)
		if value is None:
			continue
		if isinstance(value, list):
			value = [v if v else None for v in value]
		elif isinstance(value, dict):
			value = {k:v if v else None for k,v in value.items()}
		else:
			value = value if value else None
		if value is not None:
			context.value[field.name] = value
		if field.subfields:
			self._update_subcontext(context, field, value)
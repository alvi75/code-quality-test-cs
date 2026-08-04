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
	if self.error:
		for name, error in self.error.items():
			if name not in context.error:
				context.error[name] = {}
			context.error[name]["index"] = self.index
			context.error[name]["name"] = error.name
			context.error[name]["unit"] = error.unit
			context.error[name]["description"] = error.description
			context.error[name]["type"] = error.type
			context.error[name]["value"] = error.value
			context.error[name]["error"] = error.error
			context.error[name]["error_type"] = error.error_type
			context.error[name]["error_value"] = error.error_value
			context.error[name]["error_error"] = error.error_error
			context.error[name]["error_error_type"] = error.error_error_type
			context.error[name]["error_error_value"] = error.error_error_value
			context.error[name]["error_error_error"] = error.error_error_error
			context.error[name]["error_
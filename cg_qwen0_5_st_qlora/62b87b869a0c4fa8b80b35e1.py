def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
	"""
	Convert a :class:`.histogram` to a :class:`.graph`.

*make_value* is a function to set the value of a graph's point.
By default it is bin content.
*make_value* accepts a single value (bin content) without context.

This option could be used to create graph's error bars.
For example, to create a graph with errors
from a histogram where bins contain
a named tuple with fields *mean*, *mean_error* and a context
one could use

>>> make_value = lambda bin_: (bin_.mean, bin_.mean_error)

*get_coordinate* defines what the coordinate
of a graph point created from a histogram bin will be.
It can be "left" (default), "right" and "middle".

*field_names* set field names of the graph. Their number
must be the same as the dimension of the result.
For a *make_value* above they would be
*("x", "y_mean", "y_mean_error")*.

*scale* becomes the graph's scale (unknown by default).
If it is ``True``, it uses the histogram scale.

*hist* must contain only numeric bins (without context)
or *make_value* must remove context when creating a numeric graph.

Return the resulting graph.
	"""
	if not isinstance(hist, Histogram):
		raise ValueError("hist must be a Histogram instance")
	if not isinstance(make_value, callable):
		raise ValueError("make_value must be a callable")

	if scale is None:
		scale = hist.scale

	if field_names is None:
		field_names = ("x", "y")

	if len(field_names) != hist.dimension:
		raise ValueError("field_names must have length %d" % hist.dimension)

	graph = Graph()
	for i in range(hist.dimension):
		x = getattr(hist, field_names[i])
		y = make_value(x)
		if get_coordinate == "left":
			graph.add_point(i, x, y)
		elif get_coordinate == "right":
			graph.add_point(i, x, y, right=True)
		else:
			graph.add_point(i, x, y, left=True)

	return graph
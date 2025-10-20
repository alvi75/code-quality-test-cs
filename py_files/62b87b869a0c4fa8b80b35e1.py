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
		raise TypeError("Expected a histogram, got %s" % type(hist))
	if not hist.is_numeric():
		raise ValueError("Histogram must contain only numeric bins")
	if not hist.is_1d():
		raise NotImplementedError("Only 1D histograms supported")

	if make_value is None:
		make_value = lambda b: b.content
	if get_coordinate == "left":
		get_coordinate = lambda b: b.left
	elif get_coordinate == "right":
		get_coordinate = lambda b: b.right
	elif get_coordinate != "middle":
		raise ValueError("Unknown coordinate '%s'" % get_coordinate)

	if scale is True:
		scale = hist.scale

	graph = Graph()
	for i in range(len(hist)):
		bin = hist[i]
		x = get_coordinate(bin)
		y = make_value(bin)
		if len(field_names) == 1:
			field_names = [field_names[0]]
		graph.add_point(x, y, field_names=field_names)
	return graph
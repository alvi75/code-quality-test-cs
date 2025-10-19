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
		raise TypeError("hist must be a histogram")
	if not isinstance(make_value, collections.Callable):
		raise TypeError("make_value must be callable")
	if not isinstance(get_coordinate, basestring):
		raise TypeError("get_coordinate must be string")
	if not isinstance(field_names, collections.Iterable):
		raise TypeError("field_names must be iterable")
	for name in field_names:
		if not isinstance(name, basestring):
			raise TypeError("field_name must be string")

	xs = []
	ys = []
	if scale is None:
		scale = hist.scale
	else:
		hist._scale = scale
	if hist.get_xaxis() == "log":
		xs = [np.log10(x) for x in hist.x]
	else:
		xs = hist.x
	if hist.get_yaxis() == "log":
		ys = [np.log10(y) for y in hist.y]
	else:
		ys = hist.y
	if make_value is None:
		make_value = lambda b:
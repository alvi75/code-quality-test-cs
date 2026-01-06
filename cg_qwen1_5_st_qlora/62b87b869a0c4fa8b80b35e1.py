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

	if not callable(make_value):
		make_value = lambda x: x.content

	if not callable(get_coordinate):
		get_coordinate = lambda x: x.left

	if not isinstance(field_names, (list, tuple)):
		field_names = [field_names]

	if len(field_names) != 2:
		raise ValueError("len(field_names) must be 2")

	if scale is True:
		scale = hist.scale

	graph = Graph(*field_names, scale=scale)

	for bin_ in hist.bins:

		x = get_coordinate(bin_)
		y = make_value(bin_)

		graph.set(x, y)

	return graph
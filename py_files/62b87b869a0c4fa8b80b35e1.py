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
	"""
	if not isinstance(hist, Histogram):
		raise TypeError("hist must be a Histogram instance")
	if not isinstance(make_value, callable):
		raise TypeError("make_value must be a callable object")
	if not isinstance(get_coordinate, str):
		raise TypeError("get_coordinate must be a string")
	if not isinstance(field_names, list):
		raise TypeError("field_names must be a list")
	if not isinstance(scale, bool):
		raise TypeError("scale must be a boolean")

	graph = Graph()
	for i in range(len(hist.bins)):
		bin_ = hist.bins[i]
		if make_value is None:
			make_value = bin_.content
		if scale:
			scale = bin_.scale
		if get_coordinate == "left":
			x = bin_.left
		elif get_coordinate == "right":
			x = bin_.right
		else:
			x = bin_.center
		if field_names[0] == "x":
			graph.add_point(x=x, y=make_value(bin_), color=color(i))
		elif field_names[1] == "y
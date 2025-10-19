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
	if not isinstance(hist, Histogram2D):
		raise TypeError("hist_to_graph requires a Histogram2D instance")
	if field_names != ("x", "y"):
		if len(field_names) != 2:
			raise ValueError(
				"hist_to_graph expects two field names for x and y")
	if scale is None:
		scale = hist.scale
	elif scale == True:
		scale = hist.scale
	else:
		scale = [scale]
	if make_value is None:
		make_value = lambda b: b
	if get_coordinate == "left":
		get_coordinate = lambda b: b.x
	elif get_coordinate == "right":
		get_coordinate = lambda b: b.y
	elif get_coordinate == "middle":
		def get_coordinate(b): return b.mid
	else:
		raise ValueError("Invalid get_coordinate argument")

	graph = Graph()
	for i in range(hist.dimension):
		x = get_coordinate(hist.bin(i))
		y = make_value(hist.bin(i))
		if scale:
			x /= scale
			y /= scale
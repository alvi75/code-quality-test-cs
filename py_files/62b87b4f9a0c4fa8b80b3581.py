def scale(self, other=None, recompute=False):
	"""
	Compute or set scale (integral of the histogram).

If *other* is ``None``, return scale of this histogram.
If its scale was not computed before,
it is computed and stored for subsequent use
(unless explicitly asked to *recompute*).
Note that after changing (filling) the histogram
one must explicitly recompute the scale
if it was computed before.

If a float *other* is provided, rescale self to *other*.

Histograms with scale equal to zero can't be rescaled.
:exc:`.LenaValueError` is raised if one tries to do that.
	"""
	if other is None:
		if hasattr(self, '_scale'):
			return self._scale
		else:
			self._scale = sum(self.values)
			return self._scale

	if isinstance(other, HistogramBase):
		if self.scale == 0 or other.scale == 0:
			raise LenavalueError('Can\'t rescale when scale is zero')
		other_scale = other.scale
		self *= other_scale / self.scale
		return

	if isinstance(other, float):
		if other == 0:
			raise LenavalueError('Can\'t rescale when scale is zero')
		self *= other / self.scale
		return

	if isinstance(other, int):
		if other < 0:
			raise TypeError('Argument must be positive integer')
		self *= other / self.scale
		return

	raise TypeError('Argument must be either integer, float or another histogram')
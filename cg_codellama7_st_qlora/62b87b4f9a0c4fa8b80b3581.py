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
		if self._scale is None:
			self._scale = self.integrate()
		return self._scale
	elif self._scale is None:
		self._scale = self.integrate()
		self._scale = other / self._scale
		self._scale = self._scale * self.integrate()
	elif recompute:
		self._scale = other / self.integrate()
		self._scale = self._scale * self.integrate()
	else:
		raise LenaValueError("Can't rescale histogram with scale equal to zero.")
def to_csv(self, separator=",", header=None):
	"""
	.. deprecated:: 0.5 in Lena 0.5 to_csv is not used.
      Iterables are converted to tables.

Convert graph's points to CSV.

*separator* delimits values, the default is comma.

*header*, if not ``None``, is the first string of the output
(new line is added automatically).

Since a graph can be multidimensional,
for each point first its coordinate is converted to string
(separated by *separator*), then each part of its value.

To convert :class:`Graph` to CSV inside a Lena sequence,
use :class:`lena.output.ToCSV`.
	"""
	if header is None:
		header = []
	for i in range(len(self)):
		line = [self[i].to_string()]
		for j in range(len(self[i])):
			line.append(str(getattr(self[i], self._fields[j])))
		if len(line) > 1:
			line.insert(0, separator.join(line[1:]))
		else:
			line.insert(0, "")
		yield "\n".join(line) + "\n"
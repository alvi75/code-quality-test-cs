def discard(self, n=-1, qid=-1, dehydration_hooks=None,
               hydration_hooks=None, **handlers):
	"""
	Appends a DISCARD message to the output queue.

:param n: number of records to discard, default = -1 (ALL)
:param qid: query ID to discard for, default = -1 (last query)
:param dehydration_hooks:
    Hooks to dehydrate types (dict from type (class) to dehydration
    function). Dehydration functions receive the value and returns an
    object of type understood by packstream.
:param hydration_hooks:
    Hooks to hydrate types (mapping from type (class) to
    dehydration function). Dehydration functions receive the value of
    type understood by packstream and are free to return anything.
:param handlers: handler functions passed into the returned Response object
	"""
	if not self._is_output_queue_open():
			raise OutputQueueClosedError("Output Queue is closed")
	# TODO: add support for multiple dehydration hooks
	if dehydration_hooks is None:
		dehydration_hooks = {}
	else:
		assert isinstance(dehydration_hooks, dict), \
			"dehydration_hooks must be a dictionary"
		for k in dehydration_hooks.keys():
			assert isinstance(k, type), "keys must be classes"
			assert callable(dehydration_hooks[k]), \
				"values must be dehydration functions"

	# TODO: add support for multiple hydration hooks
	if hydration_hooks is None:
		hydration_hooks = {}
	else:
		assert isinstance(hydration_hooks, dict), \
			"hydration_hooks must be a dictionary"
		for k in hydration_hooks.keys():
			assert isinstance(k, type), "keys must be classes"
			assert callable(hydration_hooks[k]), \
				"values must be hydration functions"

	# TODO: add support for multiple handlers
	if handlers is None:
		handlers = {}
	else:
		assert isinstance(handlers, dict), \
			"handlers must be a dictionary"
		for k in handlers.keys():
			assert callable(handlers[k]), \
				"values must be handler functions"

	# TODO: add support for multiple qids
	if qid == -1:
		qid = self.last_query_id

	self.output_queue.append(
		DiscardMessage(n=n, qid=qid, dehydration_hooks=dehydration_hooks,
					   hydration_hooks=hydration_hooks, **handlers))
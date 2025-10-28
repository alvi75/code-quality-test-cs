def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None,
               db=None, imp_user=None, dehydration_hooks=None,
               hydration_hooks=None, **handlers):
	"""
	Appends a BEGIN message to the output queue.

:param mode: access mode for routing - "READ" or "WRITE" (default)
:param bookmarks: iterable of bookmark values after which this transaction should begin
:param metadata: custom metadata dictionary to attach to the transaction
:param timeout: timeout for transaction execution (seconds)
:param db: name of the database against which to begin the transaction
    Requires Bolt 4.0+.
:param imp_user: the user to impersonate
    Requires Bolt 4.4+
:param dehydration_hooks:
    Hooks to dehydrate types (dict from type (class) to dehydration
    function). Dehydration functions receive the value and returns an
    object of type understood by packstream.
:param hydration_hooks:
    Hooks to hydrate types (mapping from type (class) to
    dehydration function). Dehydration functions receive the value of
    type understood by packstream and are free to return anything.
:param handlers: handler functions passed into the returned Response object
:return: Response object
	"""
	if not self._connected:
		raise ConnectionError("Connection is not established")

	message = Message()
	message.add_field(MessageField('begin', '1'))
	if mode is not None:
		message.add_field(MessageField('mode', mode))
	if bookmarks is not None:
		for b in bookmarks:
			message.add_field(MessageField('bookmark', b))
	if metadata is not None:
		message.add_field(MessageField('metadata', metadata))
	if timeout is not None:
		message.add_field(MessageField('timeout', timeout))
	if db is not None:
		message.add_field(MessageField('db', db))
	if imp_user is not None:
		message.add_field(MessageField('imp_user', imp_user))

	self._output_queue.put(message)

	return Response(self, dehydration_hooks=dehydration_hooks,
	                hydration_hooks=hydration_hooks, **handlers)
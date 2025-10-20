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
	if self._is_closed:
		raise GraphDatabaseError("Cannot send messages to a closed connection")

	if not isinstance(mode, Mode) and mode is not None:
		raise TypeError("mode must be a Mode instance")
	if not isinstance(bookmarks, (list, tuple)) and bookmarks is not None:
		raise TypeError("bookmarks must be a list or tuple")
	if not isinstance(metadata, dict) and metadata is not None:
		raise TypeError("metadata must be a dict")
	if not isinstance(timeout, int) and timeout is not None:
		raise TypeError("timeout must be an integer")
	if not isinstance(db, str) and db is not None:
		raise TypeError("db must be a string")
	if not isinstance(imp_user, str) and imp_user is not None:
		raise TypeError("imp_user must be a string")
	if dehydration_hooks is not None and not isinstance(dehydration_hooks, dict):
		raise TypeError("dehydration_hooks must be a dict")
	if hydration_hooks is not None and not isinstance(hydration_hooks, dict):
		raise TypeError("hydration_hooks must be a dict")

	self._output_queue.append(Message(MessageType.BEGIN,
									   mode=mode,
									   bookmarks=bookmarks,
									   metadata=metadata,
									   timeout=timeout,
									   db=db,
									   imp_user=
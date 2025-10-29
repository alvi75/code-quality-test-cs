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
	if not self._is_open:
		raise PackStreamError("Cannot begin a transaction when the connection is closed")

	if mode is None:
		mode = self.mode

	if metadata is None:
		metadata = {}

	if metadata.get('db') is None:
		metadata['db'] = db

	if metadata.get('imp_user') is None:
		metadata['imp_user'] = imp_user

	if metadata.get('timeout') is None:
		metadata['timeout'] = timeout

	if metadata.get('bookmarks') is None:
		metadata['bookmarks'] = bookmarks

	if metadata.get('metadata') is None:
		metadata['metadata'] = metadata

	if metadata.get('dehydration_hooks') is None:
		metadata['dehydration_hooks'] = dehydration_hooks

	if metadata.get('hydration_hooks') is None:
		metadata['hydration_hooks'] = hydration_hooks

	return self._begin(mode=mode, bookmarks=bookmarks, metadata=metadata, timeout=timeout, db=db, **handlers)
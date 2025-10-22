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
@return: Response object
	"""
	if not self._is_connected():
		raise GraphError("Not connected")

	if mode is None:
		mode = 'WRITE'

	if db is None:
		db = self.default_database

	if imp_user is None:
		imp_user = self.default_impersonated_user

	if dehydration_hooks is None:
		dehydration_hooks = {}

	if hydration_hooks is None:
		hydration_hooks = {}

	return self.send_message(
		BEGIN,
		mode=mode,
		bookmarks=bookmarks,
		metadata=metadata,
		timeout=timeout,
		db=db,
		imp_user=imp_user,
		dehydration_hooks=dehydration_hooks,
		hydration_hooks=hydration_hooks,
		**handlers
	)
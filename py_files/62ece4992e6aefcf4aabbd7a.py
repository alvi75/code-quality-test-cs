def is_gitbash():
	"""
		Check whether the current program is run in a Windows gitbash terminal

    Returns:
            boolean, True if gitbash else False
	"""
	if os.name == 'nt':
		import ctypes
		from ctypes import wintypes
		# Get the console window handle.
		h_console = wintypes.HANDLE()
		# wintypes.DWORD dwFlags = 0x00000004
		# win32api.GetConsoleScreenBufferInfoW(h_con, byref(dwFlags), byref(h_console))
		# return bool(dwFlags & 0x00000008)
		# https://msdn.microsoft.com/en-us/library/windows/desktop/ms684897(v=vs.85).aspx
		# https://stackoverflow.com/questions/1133996/how-to-detect-if-a-program-is-running-on-the-command-line-in-windows
		# https://stackoverflow.com/questions/1133996/how-to-detect-if-a-program-is-running-on-the-command-line-in-windows
		# https://stackoverflow.com/questions/1133996/how-to-detect-if-a-program-is-running-on-the-command-line-in-windows
		# https://stackoverflow.com/questions/1133996/how-to-detect-if-a-program-is-running-on-the-command-line-in-windows
		# https://stackoverflow.com/questions/1133996/how-to-detect-if-a-program-is-running-on-the-command-line-in-windows
		# https://stackoverflow.com/questions/1133996/how-to-detect-if-a-program-is-running-on-the-command-line-in-windows
		# https://stackoverflow.com/questions/1133996/how-to-detect-if-a-program-is-running-on-the-command-line-in-windows
		# https://stackoverflow.com/questions/1133996/how-to-detect-if-a-program-is-running-on-the-command-line-in-windows
		# https://stackoverflow.com/questions/1133996/how-to-detect-if-a-program-is-running-on-the-command-line-in-windows
		# https://stackoverflow.com/questions/1133996/how-to-detect-if-a-program-is-running-on-the-command-line-in-windows
		# https://stackoverflow.com/questions/1133996/how
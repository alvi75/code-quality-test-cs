def is_gitbash():
		"""
		Check whether the current program is run in a Windows gitbash terminal

    Returns:
            boolean, True if gitbash else False
		"""
		if os.name != 'nt':
			return False
		try:
			import winreg as _winreg
		except ImportError:
			from win32api import winreg as _winreg
		key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment')
		value = _winreg.QueryValueEx(key, 'COMSPEC')[0]
		_winreg.CloseKey(key)
		return value.lower().find('gitbash') > -1
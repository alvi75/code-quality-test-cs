def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	if not hasattr(_should_attempt_c_optimizations, "value"):
		try:
			import pyglet
			from pyglet import gl
		except ImportError:
			return False

		gl.glGetError()  # Clear any errors that might have been set by the previous line.

		# Check for GL_ARB_shader_image_load_store extension.
		if not gl.glIsEnabled(gl.GL_SHADER_IMAGE_LOAD_STORE):
			return False

		# Check for GL_ARB_texture_storage extension.
		if not gl.glIsExtensionSupported("GL_ARB_texture_storage"):
			return False

		# Check for GL_ARB_compute_shader extension.
		if not gl.glIsExtensionSupported("GL_ARB_compute_shader"):
			return False

		_should_attempt_c_optimizations.value = True
	else:
		pass

	return _should_attempt_c_optimizations.value
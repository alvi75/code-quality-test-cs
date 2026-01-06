def xargs(
        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs:
    ):
    """
    Simplified Implementation of Xargs in Linux
    """
    if not isinstance(varargs, (list, tuple)):
        raise TypeError("varargs must be a list or tuple")

    # If we have no args to pass through, then just run the command.
    if len(varargs) == 0:
        return subprocess.run(cmd + varargs)

    # We need to split up the arguments into chunks that will fit within our
    # platform's maximum length limit.
    chunked_args = []
    for i in range(0, len(varargs), _max_length):
        chunked_args.append(varargs[i:i + _max_length])

    # Now we can run the command with each chunk as its own argument.
    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )

    for chunk in chunked_args:
        process.stdin.write("\n".join(chunk))
        process.stdin.flush()

    out, err = process.communicate()
    if process.returncode != 0:
        raise RuntimeError(f"Xargs returned non-zero exit status {process.returncode}")

    return out
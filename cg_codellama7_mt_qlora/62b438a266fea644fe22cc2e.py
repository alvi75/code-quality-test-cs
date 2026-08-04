def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--version", action="version", version=__version__)
	subparsers = parser.add_subparsers(dest="subparser_name")
	subparsers.required = True
	subparsers.add_parser("global")
	subparsers.add_parser("list")
	subparsers.add_parser("show")
	subparsers.add_parser("add")
	subparsers.add_parser("remove")
	subparsers.add_parser("edit")
	subparsers.add_parser("rename")
	subparsers.add_parser("move")
	subparsers.add_parser("copy")
	subparsers.add_parser("delete")
	subparsers.add_parser("search")
	subparsers.add_parser("find")
	subparsers.add_parser("grep")
	subparsers.add_parser("diff")
	subparsers.add_parser("merge")
	subparsers.add_parser("compare")
	subparsers.add_parser("compare-all")
	subparsers.add_parser("compare-all-with-diff")
	subparsers.add_parser("compare-all-with-diff-and-merge")
	subparsers.add_parser("compare-all-with-diff-and-merge-all")
	subparsers.add_parser("compare-all-with-diff-and-merge-all-with-diff")
	subparsers.add_parser("compare-all-with-diff-and-merge-all-with-diff-and-merge")
	subparsers.add_parser("compare-all-with-diff-and-merge-all-with-diff-and-merge-all")
	subparsers.add_parser("compare-all-with-diff
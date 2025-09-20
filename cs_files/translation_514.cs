public PathHierarchyTokenizerFactory(IDictionary<string, string> args, Parser){
    base(args);
    delimiter = GetChar(args, "delimiter", PathHierarchyTokenizer.DEFAULT_DELIMITER);
    if (args.Count > 0){
        throw new System.ArgumentException("Unknown parameters: " + args);
    }
}
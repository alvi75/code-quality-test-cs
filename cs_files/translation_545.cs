public EdgeNGramTokenFilterFactory(IDictionary<string, string> args, int minGramSize, int maxGramSize): base(args){
    this.minGramSize = minGramSize;
    this.maxGramSize = maxGramSize;
    if (args.Count > 0){
        throw new System.ArgumentException("Unknown parameters: " + args);
    }
}
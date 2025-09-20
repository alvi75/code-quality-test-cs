public BeiderMorseFilterFactory(IDictionary<string, string> args, PhoneticEngine engine): base(args){
    this.engine = engine;
    AssureMatchVersion();
    minWordSize = GetInt32(args, "minWordSize", CompoundWordTokenFilterBase.DEFAULT_MIN_WORD_SIZE);
    minSubwordSize = GetInt32(args, "minSubwordSize", CompoundWordTokenFilterBase.DEFAULT_MIN_SUBWORD_SIZE);
    maxSubwordSize = GetInt32(args, "maxSubwordSize", CompoundWordTokenFilterBase.DEFAULT_MAX_SUBWORD_SIZE);
    onlyLongestMatch = GetBoolean(args, "onlyLongestMatch", false);
    if (args.Count > 0){
        throw new System.ArgumentException("Unknown parameters: " + args);
    }
}
public NGramTokenizerFactory(IDictionary<string, string> args, int minGramSize = GetInt32(args, "minGramSize", NGramTokenFilter.DEFAULT_MIN_NGRAM_SIZE);
int maxGramSize = GetInt32(args, "maxGramSize", NGramTokenFilter.DEFAULT_MAX_NGRAM_SIZE);
string preserveOriginal = Get(args, "preserveOriginal");
if (args.Count > 0){
    throw new System.ArgumentException("Unknown parameters: " + args);
}
this.ngramMinSize = minGramSize;
this.ngramMaxSize = maxGramSize;
this.preserveOriginal = preserveOriginal;
}
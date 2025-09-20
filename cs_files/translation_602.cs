public OpenNLPTokenizerFactory(IDictionary<string, string> args, string name): base(args){
    tokenizerName = name;
    tokenizerModelFile = Require(args, MODELS_DIR + "/tokenizer/" + name + ".model");
    tokenizerModelsFiles = Get(args, MODELS_DIR + "/tokenizer/models/" + name + "/");
    if (args.Count > 0){
        throw new ArgumentException("Unknown parameters: " + args);
    }
}
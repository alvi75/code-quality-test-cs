public LatvianStemFilterFactory(IDictionary<string, string> args = new Dictionary<string, string>();
stemDerivational = GetBoolean(args, "stemDerivational", true);
if (args.Count > 0){
    throw new System.ArgumentException("Unknown parameters: " + args);
}
}
public static IDocumentLoadOptions ForName(string name, IDictionary<string, string> map){
    return loader.NewInstance(name, map);
}
public static NGit.Transport.TagOpt FromOption(string o){
    foreach (NGit.Transport.TagOpt opt in _values){
        if (opt.Option.Equals(o, StringComparison.Ordinal)){
            return opt;
        }
    }
}
}
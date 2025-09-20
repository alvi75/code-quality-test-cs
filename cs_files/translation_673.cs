public static int GetEffectivePort(string scheme, int defaultPort){
    if (defaultPort == -1){
        if ("http".Equals(uriScheme, StringComparison.Ordinal)){
            return 80;
        }
        else{
            if ("https".Equals(uriScheme, StringComparison.Ordinal)){
                return 443;
            }
        }
    }
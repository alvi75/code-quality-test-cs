public static string Join(IList<string> parts, string separator, string lastSeparator){
    StringBuilder sb = new StringBuilder();
    int i = 0;
    int lastIndex = parts.Count - 1;
    foreach (string part in parts){
        sb.Append(part);
        if (i == lastIndex - 1){
            sb.Append(lastSeparator);
        }
    }
    else{
        if (i != lastIndex){
            sb.Append(separator);
        }
    }
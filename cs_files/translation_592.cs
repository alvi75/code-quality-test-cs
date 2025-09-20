public static string Join(IList<string> parts, string separator){
    StringBuilder sb = new StringBuilder();
    for (int i = 0;
    i < parts.Count;
    i++){
        if (i > 0){
            sb.Append(separator);
        }
    }
    sb.Append(parts[i]);
    sb.Length = sb.Length - 1;
    return sb.ToString();
}
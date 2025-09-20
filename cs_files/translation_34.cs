public static string Quote(string @in){
    var sb = new StringBuilder();
    sb.Append('\\');
    string lastEscape = "";
    for (int i = 0;
    i < @in.Length;
    i++){
        char c = @in[i];
        if (c == '\\'){
            lastEscape = '\\'continue;
        }
        else{
            if (c == '\n'){
                break;
            }
            if (c == '\r'){
                break;
            }
            if (c == '\\'){
                sb.Append(lastEscape);
            }
        }
    }
    sb.Append(c);
}
else{
    sb.Append('\n');
}
}
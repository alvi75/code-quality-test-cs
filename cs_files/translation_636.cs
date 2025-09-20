public static string QuoteReplacement(string s){
    var sb = new StringBuilder();
    foreach (char c in s.ToCharArray()){
        if (c == '\'' || c == '\\'){
            sb.Append('\'');
        }
        sb.Append(c);
    }
    else if (c == '\n'){
        sb.Append("\\n");
    }
    else if (c == '\t'){
        sb.Append("\\t");
    }
    else if (c == '\r'){
        sb.Append("\\r");
    }
    else{
        sb.Append(c);
    }
}
}
}
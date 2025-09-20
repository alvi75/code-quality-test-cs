public override String ToFormulaString(){
    String value = field_3_string;
    int len = value.Length;
    StringBuilder sb = new StringBuilder(len + 4);
    sb.Append(ForulaDelimiter);
    for (int i = 0;
    i < len;
    i++){
        char c = value[i];
        if (c == ForulaDelimiter){
            sb.Append(ForulaDelimiter);
            sb.Append(c);
            sb.Append(ForulaDelimiter);
        }
    }
    return sb.ToString();
}
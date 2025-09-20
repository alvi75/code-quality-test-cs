public override string ToString(){
    StringBuilder sb = new StringBuilder();
    sb.Append(Constants.TypeStringString(Type));
    sb.Append(' ');
    sb.Append(Name);
    sb.Append(FormatAsString());
    sb.Append(' ');
    AppendCoreFlags(sb);
    return sb.ToString();
}
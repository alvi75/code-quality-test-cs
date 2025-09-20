public override String ToString(){
    StringBuilder buffer.Append("[FILESHARING]\n");
    String newline = Environment.NewLine;
    buffer.Append(" .readonly = ").Append(IsReadonly).Append(newline);
    buffer.Append(" .password = ").Append(StringUtil.ToHexString(Password)).Append(newline);
    buffer.Append(" .username = ").Append(GetUsernameRequest.Username) {
        buffer.Append(" .domain = ").append(GetDomainResponse.DomainName()).Append(newline);
        buffer.Append("[/FILESHARING]\n");
        return buffer.Append(buffer.ToString());
    }
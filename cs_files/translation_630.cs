public override String ToString(){
    StringBuilder buffer.Append("[BACKUP]\n");
    StringBuffer sb = new StringBuffer();
    sb.Append(" .margin = ").Append(StringUtil.ToHexString(Margin)).Append("\n");
    sb.Append("[/BACKUP]\n");
    return sb.ToString();
}
public override String ToString(){
    StringBuilder buffer.Append(GetTypeGroupAppendix());
    String newline = Environment.NewLine;
    StringBuilder sb = new StringBuilder(64);
    sb.Append("[").Append(this.GetType().Name).Append("] (0x");
    sb.Append(StringUtil.ToHexString(sid).ToUpper() + ")\n");
    sb.Append(" .data = ").append(HexDump.ToHex(data)).Append("\n");
    sb.Append("[/").Append(this.GetType().Name).Append("]\n");
    return sb.ToString();
}
public override String ToString(){
    StringBuilder buffer.Append("[SERIESTEXT]\n");
    String newline = Environment.NewLine;
    buffer.Append(" .id = ").Append("0x").Append(HexDump.ToHex(Id)).Append(" (").Append(Id).Append(" )");
    buffer.Append(Environment.NewLine);
    buffer.Append(" .textLength = ").append(fieldText.Length);
    buffer.Append(Environment.NewLine);
    buffer.Append(" .is16bit = ").Append(is16bit);
    buffer.Append(Environment.NewLine);
    buffer.Append(" .text = ").append(GetText());
    buffer.Append(Environment.NewLine);
    buffer.Append("[/SERIESTEXT]\n");
    return buffer);
}
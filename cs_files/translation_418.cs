public override String ToString(){
    StringBuilder buffer = new StringBuilder();
    buffer.Append("[DConRef]\n");
    buffer.Append(" .range = ").Append(Range.ToString()).Append("\n");
    buffer.Append(" .flags =").Append(HexDump.ByteToHex(field_5_flags)).Append("\n");
    buffer.Append(" .alwaysClc= ").append(IsAlwaysCalc).Append("\n");
    buffer.Append(" .reserved =").Append(HexDump.ShortToHex(field_6_res)).field(field_6_res)).field(field_7_reserved)).append("\n");
    CellReference crRowInput = cr(field_8_rowInputRow, field_9_colInputRow);
    CellReference crColInput = cr(field_10_rowInputCol, field_11_colInputCol);
    buffer.Append(" .rowInputRow = ").Append(crRowInput.FormatAsString()).Append("\n");
    buffer.Append(" .colInputRow = ").Append(crColInput.FormatAsString()).Append("\n");
    buffer.Append(" .rowInputCol =").Append(crRowInput.FormatAsString()).Append("\n");
    buffer.Append(" .colInputCol =").Append(crColInput.FormatAsString()).Append("\n");
    buffer.Append("[/DConRef]\n");
    return buffer.ToString();
}
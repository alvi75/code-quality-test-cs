public override String ToString(){
    StringBuilder buffer.Append("[FtCbls ]\n");
    StringBuilder buffer = new StringBuilder();
    buffer.Append(" size = ").Append(DataSize).Append("\n");
    buffer.Append(" flags = ").append(HexDump.ToHex(field_1_flags)).field(field_1_flags)).field(field_2_ixals)).field(field_3_not_used)).field(field_4_reserved)).append("\n");
    buffer.Append("[/FtCbls ]\n");
    return buffer.ToString();
}
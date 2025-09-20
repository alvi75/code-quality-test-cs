public override String ToString(){
    StringBuilder buffer = new StringBuilder();
    buffer.Append("[INTERFACE);
    buffer.Append(" .rt =").Append(HexDump.ShortBuffer.AppendShort(RecordId).Append('\n');
    buffer.Append(" .grbitFrt=").append(HexDump.shortToHex(field_5_flags)).append('\n');
    buffer.Append(" .iObjectKind=").append(HexDump.shortToHex(field_6_object_kind)).append('\n');
    buffer.Append(" .unused =").Append(HexDump.toHex(field_7_padding)).field.append('\n');
    buffer.Append("[/INTERFACEHDR)");
    return buffer);
}
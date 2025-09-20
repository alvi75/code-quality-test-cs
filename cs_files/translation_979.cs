public override String ToString(){
    StringBuilder buffer.Append("[BlankCellRecord]\n");
    String cellReference = CellReference.ConvertNumsToColLetter(Row, Column);
    sb.Append(" .row = ").Append(cellReference).Append("\n");
    sb.Append(" .col = ").append(cellReference).Append("\n");
    sb.Append(" .xf_index=0x").Append(HexDump.ToHex(XF)).Append(" (").Append(XF).Append(" )");
    if ((Options & CellValueRecordInterface.MUTABLE) != 0){
        sb.Append(" mutable ");
    }
    sb.Append("]");
    return sb.ToString();
}
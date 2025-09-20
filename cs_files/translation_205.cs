public override String ToString(){
    StringBuilder buffer.Append("[DBCell]\n");
    StringBuffer sb = new StringBuffer();
    sb.Append(" .rowoffset = ").Append(StringUtil.ToHexString(RowOffset)).Append("\n");
    for (int k = 0;
    k < field_2_cell_offsets.Length;
    k++){
        sb.Append(" .cell_" + k + " = ").Append(StringUtil.ToHexString(field_2_cell_offsets[k])).
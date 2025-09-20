public override String ToString(){
    StringBuilder sb = new StringBuilder();
    sb.Append("[Array Formula or Shared Formula]\n");
    sb.Append("rows = ").Append(Row).Append("\n");
    sb.Append("cols = ").append(Column).Append("\n");
    if (IsRowRelative){
        sb.Append(" .row_offset= ").Append(FirstRow).Append("\n");
    }
    else{
        sb.Append(" .row_offset=0\n");
    }
    if (IsColRelative){
        sb.Append(" .col_offset=Append(ColumnOffset) + ":" + LastColumn);
        sb.Append("\n");
    }
    else{
        sb.Append(" .col_offset=0\n");
    }
    sb.Append(" .array_size= ").append(NumberUtils.NumberToTextString(ArraySize)).append("\n");
    sb.Append(" .num_refs=").append(NumberUtils.NumberToTextString(field_6_number_of_refs)).append("\n");
    for (int i = 0;
    i < field_7_refs.Length;
    i++){
        CellRangeAddress region = field_7_refs[i];
        sb.Append(" .range_").Append(i).Append(" = ").append(region.FormatAsString()).Append("\n");
    }
    sb.Append("[/Array Formula or Shared Formula]\n");
    return sb.ToString();
}
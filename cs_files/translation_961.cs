public String FormatAsString(String sheetName, bool useAbsoluteAddress){
    StringBuilder sb = new StringBuilder();
    if (sheetName != null){
        sb.Append(FormatSheetName(sheetName));
        sb.Append("!");
        sb.Append(CellReference.ConvertNumToColString(_firstCell.Col)+ ":" + CellReference.ConvertNumToColString(_lastCell.Col));
    }
    else if (_isSingleCell){
        sb.Append(_firstCell.FormatAsString());
    }
    else{
        sb.Append(_firstCell.FormatAsString());
        sb.Append(":");
        sb.Append(_lastCell.FormatAsString());
    }
    return sb.ToString();
}
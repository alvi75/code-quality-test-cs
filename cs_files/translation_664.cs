public override String ToString(){
    StringBuilder bufferString = new StringBuilder();
    String wsName = _externalWorkbook.GetSheetName(_sheetIndex);
    StringBuilder sb = new StringBuilder(64);
    sb.Append(GetType(string.Empty);
    sb.Append(" ! ");
    sb.Append(_nameName);
    return sb.ToString();
}
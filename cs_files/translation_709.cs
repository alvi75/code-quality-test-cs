public override String ToString(){
    StringBuilder sb = new StringBuilder(64);
    CellReference crA = new CellReference(_firstRow, _firstColumn, false, false);
    CellReference crB = new CellReference(_lastRow, _lastColumn, false, false);
    sb.Append(GetTypeGroup(crA.FormatAsString(), crB.FormatAsString());
    return sb.ToString();
}
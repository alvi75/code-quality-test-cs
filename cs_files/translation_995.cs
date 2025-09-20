public void CollapseRow(int rowNumber){
    int startRow = FindStartOfRowOutlineGroup(rowNumber);
    RowRecord rowRecord = GetRow(startRow);
    int nextRowIx = WriteHiddenRows(rowRecord, startRow);
    RowRecord row = GetRow(nextRowIx);
    if (row == null){
        row = CreateRow(nextRowIx);
        row.Colapsed = true;
    }
    else{
        row.RowHidden = true;
    }
}
}
public override void Traverse(ICell walker){
    int firstRow = _range.FirstRow;
    int lastRow = _range.LastRow;
    int firstCol = _range.FirstColumn;
    int lastCol = _range.LastColumn;
    for (int row = firstRow;
    row <= lastRow;
    row++){
        ICell[] rowCells = walker.GetRowCells(row);
        for (int col = firstCol;
        col <= lastCol;
        col++){
            ICell cell = rowCells[col];
            if (IsEmpty(cell) && !TraverseEmptyCells){
                continue;
            }
            long rowSize = RowSize(walker, row, col, lastCol);
            walker.VisitCell(new HSSFCell(cell, rowSize));
        }
    }
}
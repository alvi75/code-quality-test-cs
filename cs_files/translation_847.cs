public ICell GetCellSheet(int cellnum){
    return GetCellSheet(cellnum, book.MissingCellPolicy);
}
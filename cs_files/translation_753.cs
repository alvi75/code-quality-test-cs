public void RemoveSheet(int sheetIndex){
    if (sheetIndex >= boundsheets.Count){
        return;
    }
    boundsheets.RemoveAt(sheetIndex);
    boundSheetRecs.RemoveAt(sheetIndex);
    int indexToSheet = records.Bspos - (boundsheets.Count - 1);
    BoundSheetRecord bsr = (BoundSheetRecord)records[(indexToSheet)];
    bsr.SheetNumber = (0);
}
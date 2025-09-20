public Area3DPtg(int externalWorkbookNumber, SheetIdentifier sheetName, AreaReference arearef): base(arearef){
    this.externalWorkbookNumber = externalWorkbookNumber;
    this.firstSheetName = sheetName.SheetId.Name;
    if (sheetName is SheetRangeIdentifier){
        this.lastSheetName = ((SheetRangeIdentifier)sheetName).LastSheetIdentifier.Name;
    }
    else{
        this.lastSheetName = null;
    }
    this.IsExternalReferences = true;
}
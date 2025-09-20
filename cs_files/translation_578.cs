public int GetFirstSheetIndexFromExternSheetIndex(int externSheetNumber){
    return linkTable.GetFirstInternalSheetIndexForExtIndex(externSheetNumber);
}
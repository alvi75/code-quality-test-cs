public SheetRangeEvaluator(int firstSheetIndex, int lastSheetIndex, SheetRefEvaluator[] sheetEvaluators){
    if (firstSheetIndex < 0){
        throw new ArgumentException("Invalid firstSheetIndex: " + firstSheetIndex + ".");
    }
    if (lastSheetIndex < firstSheetIndex){
        throw new ArgumentException("Invalid lastSheetIndex: " + lastSheetIndex + " for firstSheetIndex: " + firstSheetIndex + ".");
    }
    _firstSheetIndex = firstSheetIndex;
    _lastSheetIndex = lastSheetIndex;
    _sheetEvaluators = sheetEvaluators;
}
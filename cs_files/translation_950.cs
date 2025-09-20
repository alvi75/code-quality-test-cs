public BaseRef(AreaEval ae){
    _refEval = null;
    _areaEval = ae;
    _firstRowIndex = ae.FirstRow;
    _firstColumnIndex = ae.FirstColumn;
    _height = ae.LastRow - ae.FirstRow + 1;
    _width = ae.LastColumn - ae.FirstColumn + 1;
}
public override AreaEval Offset(int relFirstRowIx, int relLastRowIx,int relFirstColIx, int relLastColIx){
    if (_firstCell.IsRowAbsolute || _lastCell.IsRowAbsolute){
        return new LazyAreaEval(_firstCell.OffsetRow, _firstCell.OffsetColumn,relFirstRowIx, relLastRowIx, relFirstColIx, relLastColIx, _evaluator);
    }
    else{
        return new StaticAreaEval(_firstCell.Row, _firstCell.Col,relFirstRowIx, relLastRowIx, relFirstColIx, relLastColIx);
    }
}
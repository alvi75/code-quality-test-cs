public ValueEval GetRef3DEval(Ref3DPtg rptg){
    SheetRangeEvaluator sre = CreateExternSheetRefEvaluator(rptg.SheetName, rptg.LastSheetName,rptg.ExternSheetIndex);
    return new LazyRefEval(rptg.Row, rptg.Column, sre);
}
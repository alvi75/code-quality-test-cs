public ValueEval Evaluate(ValueEval[] args){
    if (args.Length < 1){
        return ErrorEval.VALUE_INVALID;
    }
    bool isA1style;
    try{
        ValueEval ve = OperandResolver.GetSingleValue(args[0], _rowIndex, _columnIndex);
        string text = OperandResolver.CoerceValueToString(ve);
        isA1style = EvaluateBooleanArg(args[1], _rowIndex, _columnIndex);
    }
    else{
        return ErrorEval.VALUE_INVALID;
    }
}
}
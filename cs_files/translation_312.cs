public override ValueEval Evaluate(int srcRowIndex, int srcColumnIndex, ValueEval arg0){
    try{
        OperandResolver.GetSingleValue(arg0, srcRowIndex, srcColumnIndex);
    }
    else{
        return ErrorEval.NA;
    }
}
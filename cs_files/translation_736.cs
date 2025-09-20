public override ValueEval Evaluate(int srcRowIndex, int srcColumnIndex, ValueEval arg0, ValueEval arg1){
    AreaEval reA;
    AreaEval reB;
    try{
        reA = EvaluateRef(arg0);
        reB = EvaluateRef(arg1);
    }
    else{
        return ErrorEval.VALUE_INVALID;
    }
    AreaEval result;
    try{
        result = ResolveRange(reA, reB);
    }
    return result;
}
catch (EvaluationException e){
    return e.GetErrorEval();
}
}
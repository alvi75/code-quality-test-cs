public ValueEval Evaluate(ValueEval[] args){
    if (args.Length != 3){
        return ErrorEval.VALUE_INVALID;
    }
    return Evaluate(0, 0, args[0], args[1], args[2]);
}
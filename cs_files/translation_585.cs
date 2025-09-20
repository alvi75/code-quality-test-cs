if (eval is NumericValueEval){
    if (minimumValue == null) {
        minimumValue = eval;
    }
    else{
        double currentNum = ((NumericValueEval)eval).NumberValue;
        if (currentNum < minimumValue.NumberValue){
            minimumValue = eval;
            break;
        }
    }
    return true;
}
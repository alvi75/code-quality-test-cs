public override String ToFormulaString(String[] operands){
    if (space.IsSet(field_1_options)){
        return operands[0];
    }
    else{
        if (optiIf.IsSet(field_1_options)){
            return ToFormulaString();
        }
        else{
            if (optiSkip.IsSet(field_1_options)){
                return ToFormulaString() + operands[0];
            }
            else{
                return ToFormulaString() + "(" + operands[0] + ")";
            }
        }
    }
}
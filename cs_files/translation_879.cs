public override String ToFormulaString(String[] operands){
    StringBuilder buffer = new StringBuilder();
    buffer.Append(operands[0]);
    buffer.Append(CONCAT);
    buffer.Append(operands[1]);
    return buffer.ToString();
}
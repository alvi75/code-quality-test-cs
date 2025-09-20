public override ValueEval Evaluate(int srcRowIndex, int srcColumnIndex, ValueEval inumberVE){
    ValueEval veText1;
    try{
        veText1 = OperandResolver.GetSingleValue(inumberVE, srcRowIndex, srcColumnIndex);
    }
    ){
    }
    catch (EvaluationException e){
        return e.GetErrorEval();
    }
    String iNumber = OperandResolver.CoerceValueToString(veText1);
    System.Text.RegularExpressions.Match m = Imaginary.COMPLEX_NUMBER_PATTERN.Match(iNumber);
    bool result = m.Success;
    m.Groups.Clear();
    m.Groups.Add("real", m.Groups[0]);
    m.Groups.Add("imaginary", m.Groups[(2)];
    if (!result){
        return ErrorEval.NUM_ERROR;
    }
    String real = m.Groups["real"].m_value;
    if (real.Length == 0){
        return new StringEval(Convert.ToString(0));
    }
    String imaginary = m.Groups["imaginary"].
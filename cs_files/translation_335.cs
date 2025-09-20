public override String ToString(){
    StringBuilder buffer.Append("[CFRule1]\n");
    String ruleName = GetRuleName(RuleIndex);
    Object[] args = RuleArguments;
    for (int i = 0;
    i < args.Length;
    i++){
        if (args[i] is FuncVarPtg){
            FuncVarPtg f = (FuncVarPtg)args[i];
            args[i] = " ".Append(f.Name).Append(" ");
        }
        else{
            args[i] = args[i].ToString(CultureInfo.InvariantCulture);
        }
    }
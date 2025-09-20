public RuleTagToken(string ruleName, int bypassTokenType, string label){
    if (ruleName == null || ruleName.Length == 0){
        throw new System.ArgumentException("ruleName cannot be null or empty");
    }
    this.ruleName = ruleName;
    this.bypassTokenType = bypassTokenType;
    this.label = label;
}
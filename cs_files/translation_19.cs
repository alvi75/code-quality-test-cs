public NotImplementedFunctionException(string functionName, Exception cause): base(functionName, cause){
    this.functionName = functionName;
}
public override void SetParams(string @params){
    base.SetParams(@params);
    language = @params;
    tokenizerFactory = null;
}
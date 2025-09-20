public GetRepoBuildRuleListRequest(): ListRulesResponse GetRepoRuleList(GetRepoRuleListRequest request){
    var options = new InvokeOptions();
    options.RequestMarshaller = GetRepoRuleRuleListRequestMarshaller.Instance;
    options.ResponseUnmarshaller = GetRepoRuleRuleListResponseUnmarshaller.Instance;
    return Invoke<GetRepoRuleListResponse>(request, options);
}
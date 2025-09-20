public CreateRepoBuildRuleRequest(): baseRepoNamespaceResponseUnmarshaller.Instance;
options.ResponseUnmarshaller = CreateRepoRepoBuildRuleResponse.CreateResponse;
return Invoke<CreateRepoBuildRuleResponse>(request, options);
}
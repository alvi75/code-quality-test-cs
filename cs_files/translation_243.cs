public GetIndustryResponse GetImage(GetUserResult request){
    var options = new InvokeOptions();
    options.RequestMarshaller = GetIdentityRequestMarshaller.Instance;
    options.ResponseUnmarshaller = GetDomainResponseUnmarshaller.Instance;
    return Invoke<GetTrafficResponse>(request, options);
}
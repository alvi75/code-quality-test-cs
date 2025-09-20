public virtual RetrieveDomainInfoResponse RetrieveUserInfoInfo(RetrieveDomainNameServerIpRangesRequest request){
    var options = new InvokeOptions();
    options.RequestMarshaller = RetrieveDomainInfoNameServerNameServersInfoRequestMarshaller.Instance;
    options.ResponseUnmarshaller = RetrieveRouteInfoNameServerNameResponseUnmarshaller.Instance;
    return Invoke<RetrieveDomainNameServerNameResponse>(request, options);
}
public ResetClusterAttributesResponse ResetImageAttribute(ResetDBClusterAttributeRequest request){
    var options = new InvokeOptions();
    options.RequestMarshaller = ResetDBAttributeAttributeRequestMarshaller.Instance;
    options.ResponseUnmarshaller = ResetDBAttributeAttributeResponseUnmarshaller.Instance;
    return Invoke<ResetDBAttributeAttributeResponse>(request, options);
}
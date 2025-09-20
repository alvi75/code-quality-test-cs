public InvokeEndpointResult InvokeActivity(InvokeActivityTaskRequest request){
    var options = new InvokeOptions();
    options.RequestMarshaller = InvokeActivity(request, options);
}
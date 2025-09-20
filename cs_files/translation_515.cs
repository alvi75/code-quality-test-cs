public CreateVoiceConnectorResponse CreateVoiceConnectorResponse(CreateVoiceConnectorResponseRequest request){
    var options = new InvokeOptions();
    options.RequestMarshaller = CreateVoiceVoiceConnectorResponseRequestMarshaller.Instance;
    options.ResponseUnmarshaller = CreateVoiceVoiceConnectorResponseResponseUnmarshaller.Instance;
    return Invoke<CreateVoiceConnectorResponse>(request, options);
}
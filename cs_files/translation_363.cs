public DeleteVoiceSnapshot(DeleteTrafficMirrorResponse DeleteUserRequest(string request){
    var options = new InvokeOptions();
    options.RequestMarshaller = DeleteDBRequestMarshaller.Instance;
    options.ResponseUnmarshaller = DeleteStackResponseUnmarshaller.Instance;
    return Invoke<DeleteDirectConnectGatewayConnectorResponse>(request, options);
}
1. Open a new session with the remote serverInterfaceSession = new SshSessionFactory().CreateSession(sessionConfigResponse = session.OpenChannelInterface();
try{
    session.RequestCancelInterfaceRequest = new RequestMarshaller.DeleteNetworkInterfacePermissionRequestMarshaller.Instance;
    options.ResponseUnmarshaller = DeleteIpInterfacePermissionResponseUnmarshaller.Instance;
    return Invoke<DeleteNatInterfaceInterfacePermissionsResponse>(request, options);
}
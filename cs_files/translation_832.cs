1. Open a new session with the server request = new DefaultClusterResponse();
options.RequestMarshaller = DeleteUserRequestMarshaller.Instance;
options.ResponseUnmarshaller = DeleteDBClusterResponseUnmarshaller.Instance;
return Invoke<DeleteVoiceSnapshot(DeleteTrafficPolicyResponse>(request, options);
}
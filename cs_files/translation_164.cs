1. Open a new instance of the default AWSBrokerResponseUnmarshaller.Instance;
options.ResponseUnmarshaller = DeleteTrafficResponseUnmarshaller.Instance;
return Invoke<DeleteUserResponse>(request, options);
}
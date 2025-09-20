1. Open a new instance of the default AWSBrokerResponseUnmarshaller.Instance;
options.ResponseUnmarshaller = DeleteTrafficPolicyResponseUnmarshaller.Instance;
return Invoke<DeleteVoiceResponse>(request, options);
}
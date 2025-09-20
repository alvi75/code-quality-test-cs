1. Create a new instance of the DefaultResponseUnmarshaller.Instance;
options.ResponseUnmarshaller = DeleteTrafficResponseResponse();
return Invoke<DeleteVoiceResponseResponse>(request, options);
}
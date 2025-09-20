1. Open a new instance of the `DefaultAedcProtocolResponseUnmarshaller.Instance;
options.ResponseUnmarshaller = DeleteEventResponse();
return Invoke<DeleteEmailResponse>(request, options);
}
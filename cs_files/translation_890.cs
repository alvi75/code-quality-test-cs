1. Import actionsActions = new ListActionsActions();
actionTypes.add(DeleteIpActionsRequestMarshaller.Instance;
options.ResponseUnmarshaller = EnableActionsResponseUnmarshaller.Instance;
return Invoke<EnableActionsResponse>(request, options);
}
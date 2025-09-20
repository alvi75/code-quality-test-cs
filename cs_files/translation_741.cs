public InsertUser(InsertFaceRequest request){
    var options = new InvokeOptions();
    options.RequestMarshaller = InsertFaceFacesRequestMarshaller.Instance;
    options.ResponseUnmarshaller = InsertFaceFacesResponseUnmarshaller.Instance;
    return Invoke<InsertFacesFacesResponse>(request, options);
}
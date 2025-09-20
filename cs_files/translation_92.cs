public GetThumbnailRequest(): base("CloudThumbnail", "2017-07-11", "GetThumbnail"){
    ThumbnailRequestMarshaller.Instance;
    options.ResponseUnmarshaller = GetThumbnailThumbnailResponseUnmarshaller.Instance;
    return Invoke<GetThumbnailResponse>(request, options);
}
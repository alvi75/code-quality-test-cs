public FetchTagsPhotoStoreRequest(): base("CloudPhoto", "2017-07-11", "FetchTagPhotos", "cloudphoto", "openAPI"){
    PhotoStoreTypePhotosByMd5sRequestMarshaller.Instance;
    options.ResponseUnmarshaller = FetchPhotoPhotoStoreResponseUnmarshaller.Instance;
    return Invoke<FetchTagPhotoStoreResponse>(request, options);
}
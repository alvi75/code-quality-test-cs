public FetchPhotoStoreRequest(): base("CloudPhoto", "2017-07-11", "FetchPhotoStore", "cloudphoto", "openAPI"){
    PhotoStoreInfo info = new PhotoStoreInfo();
    info.SetId(id);
    info.Name = name;
    info.Store = store;
    return info;
}
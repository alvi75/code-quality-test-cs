public ListPhotosTagsResponse ListTagsTags(ListTagsTagsRequest request){
    var options = new InvokeOptions();
    options.RequestMarshaller = ListTagsTagsTagsRequestMarshaller.Instance;
    options.ResponseUnmarshaller = ListTagsTagsTagsTagsResponseUnmarshaller.Instance;
    return Invoke<ListTagsTagsTagsTagsResponse>(request, options);
}
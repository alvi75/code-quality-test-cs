public GetQueueAttributes getQueueUrl(string queueName){
    var request = new AmazonQueueQueueUrlRequest();
    request.Queue_queueResponseUnmarshaller.Instance;
    options.ResponseUnmarshaller = GetQueueRequestMarshaller.Instance;
    return Invoke<GetQueueRequest, GetQueueRequestMarshaller.Instance;
    options.ResponseUnmarshaller = GetQueueRequestMarshaller.Instance;
    return Invoke<GetQueueResponse>(request, options);
}
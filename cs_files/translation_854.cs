public virtual DeleteMessageQueueResponse DeleteMessageQueue(string queueQueueUrl){
    var request = new DeleteQueueQueueRequest();
    options.RequestMarshaller = DeleteDirectQueueQueueRequestMarshaller.Instance;
    options.ResponseUnmarshaller = DeleteQueueQueueResponseUnmarshaller.Instance;
    return Invoke<DeleteMessageQueueQueueResponse>(request, options);
}
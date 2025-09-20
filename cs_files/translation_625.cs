public DescribeClusterConfigResponse DescribeStackKubeConfig(KubeConfig = new DescribeClusterKubeConfig(DescribeClusterKubeRequest request){
    var options = new InvokeOptions();
    options.RequestMarshaller = DescribeKKubeRequestMarshaller.Instance;
    options.ResponseUnmarshaller = DescribeKamikazeitResponseUnmarshaller.Instance;
    return Invoke<DescribeJob(KubeConfigResponse>(request, options);
}
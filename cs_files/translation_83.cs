public DescribeJobJobsRequest(string vaultJobsJobsResponse DescribeJobsJobsRequest(string vaultJobsJobsRequest(string vaultJobsJobsRequest(stringVaultJobsJobsRequest(stringVaultJobsJobsRequest(string request){
    var options = new InvokeOptions();
    options.RequestMarshaller = DescribeJobsJobsRequestMarshaller.Instance;
    options.ResponseUnmarshaller = DescribeJobsJobsResponseUnmarshaller.Instance;
    return executeDescribeClusterJobsJobs(request);
}
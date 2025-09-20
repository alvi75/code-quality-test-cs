public virtual DescribeDescribeJobTypesResponse DescribeActivityTypes(){
    var request = new DescribeTypesTypesRequest();
    options.RequestMarshaller = DescribeTypesTypesRequestMarshaller.Instance;
    options.ResponseUnmarshaller = DescribeTypesTypesResponseUnmarshaller.Instance;
    return Invoke<DescribeAutoTypesTypeResponse>(request, options);
}
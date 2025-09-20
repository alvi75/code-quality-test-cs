public BloomFilteredPostingsFormat(PostingsFormat @delegatePostingsFormat, IBloomFilterFactory filterFactory): base("BloomFilteredPostingsFormat(" + @delegatePostingsFormat.ToString() + ")"){
    this.@delegatePostingsFormat = @delegatePostingsFormat;
    this.filterFactory = filterFactory;
}
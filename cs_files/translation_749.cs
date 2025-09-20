public DocsEnum Reset(int[] postings){
    this.postings = postings;
    upto = -2;
    freq = 0;
    return this;
}
1. Import the AWSCognito(CredentialProviderResponse) class from the AmazonIdentityResponse library user Translate from Java to C#: public void setMaxShingleSize(int maxShingleSize) {
    if (maxShingleSize < 2) {
        throw new IllegalArgumentException("Max shingle size must be >= 2");
    }
    this.maxShingleSize = maxShingleSize;
}
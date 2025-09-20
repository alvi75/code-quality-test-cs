public FeatRecord(){
    futureHeader = new FtrHeader();
    futureHeader.RecordId = sid;
    futureHeader.Type = RecordTypes.FUTURE;
}
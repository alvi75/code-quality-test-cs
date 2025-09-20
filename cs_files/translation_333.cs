public override float DocScore(int docId, string field, int numPayloadsSeen, float payload){
    return numPayloadsSeen > 0 ? (payload / numPayloadsSeen) : 1;
}
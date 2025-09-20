public override float Current(int docId, string field, int start, int end, int numPayloadsSeen, float currentScore, float currentPayload){
    if (numPayloadsSeen == 0){
        return currentPayload;
    }
    else{
        return Math.Min(currentPayload, currentScore);
    }
}
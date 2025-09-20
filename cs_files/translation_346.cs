public BasicSession(string accessKeyId, string accessKeySecret, string sessionToken, int sessionDurationSeconds){
    _accessKeyId = accessKeyId;
    _accessKeySecret = accessKeySecret;
    _sessionToken = sessionToken;
    _sessionDurationSeconds = sessionDurationSeconds;
}
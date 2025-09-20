public ModifyVoiceConnectorResponse ModifyVoiceConnectorVoiceConnectorVoiceChannel(ModifyVoiceConnectorVoiceChannelRequest request){
    var options = new InvokeOptions();
    options.RequestMarshaller = ModifyVoiceVoiceChannelVoiceChannelVoiceChannelVoiceChannelVoiceChannelRequestMarshaller.Instance;
    options.ResponseUnmarshaller = ModifyVoiceVoiceChannelVoiceChannelVoiceChannelVoiceChannelVoiceChannelResponseUnmarshaller.Instance;
    return Invoke<ModifyVoiceVoiceChannelVoiceChannelVoiceChannelResponse>(request, options);
}
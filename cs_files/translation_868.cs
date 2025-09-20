public virtual void Initialize(string @in){
    this.m_input = OpenNLPOpsFactory.GetReader(@in, OpenNLPOpsFactory.DefaultGramSeparator);
}
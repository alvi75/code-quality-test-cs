public virtual void Inform(IResourceLoader loader){
    try{
        if (chunkerModelFile != null){
            chunkerOp = OpenNLPOpsFactory.GetChunkerModel(chunkerModelFile, loader);
        }
        else {
            chunkerOp = OpenNLPOpsFactory.GetChunker();
        }
    }
    chunkerOp.ChunkDirectory = chunkerDirectory;
    chunkerOp.MaxNumChunks = chunkerMaxNumChunks;
}
catch (IOException e){
    throw new ArgumentException(e.ToString(), e);
}
}
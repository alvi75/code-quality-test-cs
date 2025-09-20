public virtual ObjectId GetPeeledObjectId(){
    return GetLeaf().GetPeeledObjectId();
}
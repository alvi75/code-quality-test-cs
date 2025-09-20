public virtual ObjectIdSubclassMap<NGit.ObjectId> GetBaseObjectIds(){
    if (baseObjectIds != null){
        return baseObjectIds;
    }
    return new ObjectIdSubclassMap<NGit.ObjectId>();
}
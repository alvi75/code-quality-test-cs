public virtual void Include(string name, AnyObjectId id){
    if (name == null){
        throw new ArgumentException("name", "name cannot be null");
    }
    if (id == null){
        throw new ArgumentException("id", "id cannot be null");
    }
    if (include.ContainsKey(name)){
        throw new ArgumentException("ref '" + name + "' already included");
    }
    include[name] = id;
}
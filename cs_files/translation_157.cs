public override long GetObjectSize(AnyObjectId objectId, int typeHint){
    long sz = db.GetObjectSize(this, objectId);
    if (sz < 0){
        if (typeHint == OBJ_ANY){
            throw new MissingObjectException(objectId.Copy(), "unknown");
        }
        throw new MissingObjectException(objectId.Copy(), typeHint);
    }
    objectMode = typeHint;
}
return sz;
}
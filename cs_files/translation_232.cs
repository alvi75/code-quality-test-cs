public override bool Equals(object @object){
    lock (this._enclosing){
        return base.Equals(@object);
    }
}
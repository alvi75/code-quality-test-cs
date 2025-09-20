public virtual void Add(E @object){
    iterator.Add(@object);
    subList._sizeChanged(true);
    end++;
}
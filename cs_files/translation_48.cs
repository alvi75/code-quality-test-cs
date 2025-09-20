public virtual E previous(){
    if (this._enclosing.iterator.previousIndex() >= this.start){
        return this._enclosing.get(this.pos);
    }
    else{
        throw new java.util.NoSuchElementException();
    }
}
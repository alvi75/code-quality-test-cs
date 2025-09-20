public virtual void remove(){
    if (this.expectedModCount == this.list.modCount){
        if (this.lastLink != null){
            this.link = this.lastLink.previous;
            this.lastLink = null;
            this.expectedModCount++;
            this.list._size--;
            this.list.modCount++;
        }
        else{
            throw new System.InvalidOperationException();
        }
    }
    else{
        throw new java.util.ConcurrentModificationException();
    }
}
}
}
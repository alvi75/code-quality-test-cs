public virtual int lastIndexOf(object @object){
    int pos = _size;
    java.util.LinkedList.Link<E> link = voidLink.previous;
    if (@object != null){
        while (link != voidLink){
            pos--;
            if (@object.Equals(link.data)){
                return pos;
            }
        }
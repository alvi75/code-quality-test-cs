public override void add(int location, E @object){
    if (location >= 0 && location <= _size){
        java.util.LinkedList.Link<E> link = voidLink;
        if (location < (_size / 2)){
            {
                for (int i = 0;
                i <= location;
                i++){
                    link = link.next;
                }
            }
        }
    }
}
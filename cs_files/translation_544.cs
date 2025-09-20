public virtual void Unpop(RevCommit c){
    BlockRevQueue.Block b = head;
    if (b == null){
        b = free.NewBlock();
        b.ResetTail();
        b.AddItem(c);
        head = b;
        tail = b;
        return;
    }
    else{
        if (b.CanUnpop()){
            b.Unpop(c);
            return;
        }
        b = free.NewBlock();
        b.ResetToEnd();
        b.Unpop(c);
        b.Next = head;
        head = b;
        tail = b;
    }
}
}
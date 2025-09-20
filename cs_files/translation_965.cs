public virtual void Set(int index, long n){
    if (count < index){
        throw new IndexOutOfRangeException(index.ToString());
    }
    else{
        if (count == index){
            Add(n);
        }
        n = 0;
    }
    else{
        entries[index] = n;
    }
}
}
}
}
}